#!/usr/bin/env python3

"""Ex__4_finetune.py: Answer to Ch 15 Ex 4."""

# This script fine-tunes GPT-2 (medium) using LoRA adapters
# on technical datasets.

# ========================================================
# 1.  Install and import dependencies
# ========================================================
# Install the required packages at a command prompt with
# this command:
# pip install torch transformers datasets peft accelerate
#     bitsandbytes hf_xet --upgrade

import torch
import time
from datasets import (
    Dataset,
    load_dataset,
    concatenate_datasets
)
from dataclasses import dataclass
from typing import Any, Dict, List
from peft import LoraConfig, get_peft_model
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments
)

# ========================================================
# 2.  Configuration and constants
# ========================================================

start_time = time.time()

SEED = 8675309
MAX_ARXIV = 5000
MAX_STACK = 5000
MODEL_NAME = "gpt2-medium"
OUTPUT_DIR = "./results"
MIN_TEXT_LENGTH = 100
USE_CUDA = torch.cuda.is_available()

torch.manual_seed(SEED)
if USE_CUDA:
    torch.cuda.manual_seed_all(SEED)

# ========================================================
# 3.  Helper function for status messages
# ========================================================

def print_elapsed_time(message):
    elapsed_time = int(time.time() - start_time)
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60
    print(
        f"{message}; Elapsed time: "
        f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    )

# ========================================================
# 4.  Load and prepare the datasets
# ========================================================

print("[*] Loading datasets...")

# AI keywords for filtering
ai_keywords = [
    "neural network", "machine learning", "deep learning",
    "transformer", "attention mechanism",
    "backpropagation", "gradient descent",
    "reinforcement learning", "large language model",
    "llm", "gpt", "training data", "weights",
    "fine-tuning", "lora", "embedding", "tokenizer",
    "cuda", "gpu", "tpu", "inference", "pytorch"
]

def contains_ai_keyword(text):
    return any(keyword in text.lower() for
               keyword in ai_keywords)

def collect_relevant_texts(stream, target_count: int,
                           dataset_name: str) -> List[str]:
    print(
        f"[*] Processing {dataset_name} dataset "
        f"(target: {target_count:,} records)..."
    )
    kept: List[str] = []

    for i, item in enumerate(stream):
        if len(kept) >= target_count:
            break

        text = item.get("text")
        if (
                text and len(text) >= MIN_TEXT_LENGTH and
                contains_ai_keyword(text)
        ):
            kept.append(text)

        if (i + 1) % 5000 == 0:
            print(
                f"    Processed {i + 1:,} records, "
                f"filtered to {len(kept):,}..."
            )

    print(
        f"[*] {dataset_name} complete: "
        f"{len(kept):,} records"
    )
    return kept

arxiv_stream = load_dataset(
    "common-pile/arxiv_papers",
    split="train", streaming=True
)
arxiv_texts = collect_relevant_texts(
    arxiv_stream, MAX_ARXIV, "arxiv"
)

stack_stream = load_dataset(
    "common-pile/stackexchange_filtered",
    split="train", streaming=True
)
stack_texts = collect_relevant_texts(
    stack_stream, MAX_STACK, "stack"
)

print("[*] Converting to datasets...")
arxiv_ds = Dataset.from_dict({"text": arxiv_texts})
stack_ds = Dataset.from_dict({"text": stack_texts})

print(f"    arxiv dataset: {len(arxiv_ds):,} rows")
print(f"    stack dataset: {len(stack_ds):,} rows")

# ========================================================
# 5.  Merge and shuffle the datasets
# ========================================================

combined = concatenate_datasets(
    [arxiv_ds, stack_ds]
).shuffle(seed=SEED)

print(f"[*] Filtered dataset size: {len(combined):,}")
example_text = combined.select([0])[0]['text'][:400]
print(
    f"[*] Example text (first 400 chars):\n"
    f"{example_text}\n"
)
print_elapsed_time("[*] Dataset merge complete")

# ========================================================
# 6.  Tokenize the dataset
# ========================================================

print("[*] Tokenizing...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

def tokenize_function(examples):
    tokens = tokenizer(
        examples["text"],
        truncation=True,
        max_length=256,
        padding=False
    )
    tokens["labels"] = tokens["input_ids"]
    return tokens

tokenized_ds = combined.map(
    tokenize_function,
    batched=True, remove_columns=["text"]
)

print_elapsed_time("[*] Tokenizing complete")

# ========================================================
# 7.  Load GPT-2 and apply the LoRA configuration
# ========================================================

print("[*] Loading GPT-2 model and applying LoRA...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["c_attn", "c_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    fan_in_fan_out=True,
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
print_elapsed_time("[*] GPT-2 model loading complete")

# ========================================================
# 8.  Define training parameters
# ========================================================

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=2,
    fp16=USE_CUDA,
    logging_steps=50,
    save_steps=200,
    save_total_limit=2,
    report_to="none",
    learning_rate=2e-4,
    warmup_steps=100,
    dataloader_pin_memory=USE_CUDA,
)

# ========================================================
# 9.  Train the model
# ========================================================

print("[*] Starting training...")

# Create a simple data collator that pads dynamically
@dataclass
class DataCollatorForCausalLM:
    tokenizer: Any

    def __call__(
            self, features: List[Dict[str, Any]]
    ) -> Dict[str, torch.Tensor]:
        # Extract input_ids and labels
        input_ids = [f["input_ids"] for f in features]
        labels_list = [f["labels"] for f in features]

        # Find max length in this batch
        max_length = max(len(ids) for ids in input_ids)

        # Pad sequences
        padded_input_ids = []
        padded_labels = []
        attention_mask = []

        for ids, labels in zip(input_ids, labels_list):
            padding_length = max_length - len(ids)

            # Pad input_ids with pad_token_id
            padded_input_ids.append(
                ids + [self.tokenizer.pad_token_id] *
                padding_length
            )

            # Pad labels with -100 (ignored in loss calc)
            padded_labels.append(
                labels + [-100] * padding_length
            )

            # Create an attention mask (1=tokens, 0=pad)
            attention_mask.append(
                [1] * len(ids) + [0] * padding_length
            )

        return {
            "input_ids": torch.tensor(
                padded_input_ids, dtype=torch.long
            ),
            "attention_mask": torch.tensor(
                attention_mask, dtype=torch.long
            ),
            "labels": torch.tensor(
                padded_labels, dtype=torch.long
            )
        }

data_collator = DataCollatorForCausalLM(
    tokenizer=tokenizer)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds,
    data_collator=data_collator,
)

trainer.train()
print_elapsed_time("[*] Training complete")

# ========================================================
# 10.  Save the model and the tokenizer
# ========================================================

print("[*] Saving model and tokenizer...")
model.save_pretrained("gpt2-lora-tech")
tokenizer.save_pretrained("gpt2-lora-tech")
print_elapsed_time(
    "[+] Fine-tuning complete! "
    "Model saved to ./gpt2-lora-tech"
)

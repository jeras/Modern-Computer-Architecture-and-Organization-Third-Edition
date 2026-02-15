#!/usr/bin/env python3

"""Ex__4_compare.py: Answer to Ch 15 Ex 4."""

# Compares the outputs of:
#   1. Base GPT-2 Medium
#   2. Fine-tuned GPT-2 LoRA model (gpt2-lora-tech)
#
# This program highlights improvements in technical content
# after fine-tuning on Arxiv + StackExchange data.

from transformers import AutoTokenizer, pipeline
import torch

# ========================================================
# 1. Load both of the models
# ========================================================

MODEL_BASE = "gpt2-medium"
MODEL_FINE = "./gpt2-lora-tech"

print("* Loading models...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_BASE)
tokenizer.pad_token = tokenizer.eos_token

device = 0 if torch.cuda.is_available() else -1

pipe_base = pipeline(
    "text-generation",
    model=MODEL_BASE,
    tokenizer=tokenizer,
    device=device
)

pipe_fine = pipeline(
    "text-generation",
    model=MODEL_FINE,
    tokenizer=tokenizer,
    device=device
)

# ========================================================
# 2. Define the comparison prompts
# ========================================================

prompts = [
    "Explain how gradient descent works and why learning "
    "rate selection is important.",
    "What are attention mechanisms and why did they "
    "revolutionize deep learning?",
    "Describe the process of backpropagation in a simple "
    "feedforward neural network.",
    "How do transformers handle long-range dependencies?",
    "What is the purpose of dropout, and how does it help "
    "prevent overfitting?",
    "Explain how the softmax function is used in "
    "classification models.",
    "Describe how GPUs accelerate deep learning training "
    "compared to CPUs.",
    "What are the main challenges of training large "
    "language models?",
    "Explain the difference between pre-training and "
    "fine-tuning in large models.",
    "How does quantization improve inference efficiency "
    "for neural networks?",
    "Explain the concept of parameter-efficient "
    "fine-tuning such as LoRA.",
    "Describe how tensor parallelism and model sharding "
    "enable large-scale training.",
    "What are the tradeoffs between accuracy and "
    "computational cost in model design?",
    "What are the main sources of bias in AI models, and "
    "how can they be mitigated?",
    "Explain the role of mixed precision training in "
    "accelerating AI workloads."
]

# ========================================================
# 3. Generation parameters
# ========================================================

GEN_KWARGS = dict(
    max_new_tokens=120,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

# ========================================================
# 4. Run both models and print the results
# ========================================================

print("\n>> Comparing base GPT-2 and fine-tuned GPT-2\n")

for i, prompt in enumerate(prompts, start=1):
    print("=" * 70)
    print(f"[Prompt {i}]: {prompt}\n")

    base_out = pipe_base(prompt, **GEN_KWARGS)[0][
        "generated_text"]
    fine_out = pipe_fine(prompt, **GEN_KWARGS)[0][
        "generated_text"]

    # Clean up outputs slightly
    base_out = base_out.strip().replace("\n", " ")
    fine_out = fine_out.strip().replace("\n", " ")

    print("- Base GPT-2 Output:")
    print(base_out)
    print("\n- Fine-Tuned GPT-2 Output:")
    print(fine_out)
    print("\n")

print("=" * 70)
print("** Comparison complete. Observe clarity, factual "
      "accuracy, and domain focus improvements.")


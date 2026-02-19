__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 4

Perform LoRA fine-tuning on the GPT-2 medium LLM to increase its ability to answer questions about neural networks and AI computing. Provide relevant prompts on these subjects to the original model and the fine-tuned version to determine the effects of the fine-tuning.

# Answer
This example uses publicly available datasets containing scientific papers from the _arXiv.org_ e-print archive and technical discussions from the _Stack Exchange_ network of question-and-answer sites. Data from these sources is filtered to include only topics that appear to be related to neural networks and AI computing. The resulting dataset is then used to fine-tune the GPT-2 model using the LoRA method.

With a capable GPU such as an RTX 3090, training typically completes in about an hour. On a standard PC or laptop without a GPU, the same process may require 24 hours or longer. Ensure there is at least 10 GB of available disk space for processing the dataset.

This program automates the entire process, from dataset collection and filtering to fine-tuning and saving the customized model.

[Ex__4_finetune.py](Code%20Files/Ex__4_finetune.py)

After training is complete, run the original and fine-tuned versions of the model with relevant prompts and display the results for comparison. This program presents 15 prompts to both models and displays their outputs.

[Ex__4_compare.py](Code%20Files/Ex__4_compare.py)
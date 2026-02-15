__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15: Large Language Model Computing Architectures

This chapter explores computing architectures used for advanced artificial intelligence systems, with a focus on Large Language Models. To set the stage, we begin with a breakdown of early LLM designs, using GPT-2 as a case study to illustrate model structure and processing requirements. The discussion then expands to the computational architectures used for both LLM training and inference. The chapter concludes with an examination of the data center infrastructure underpinning today’s largest and most sophisticated models, emphasizing the operational resources these facilities require, including electrical power and thermal management systems.

After completing this chapter, you will understand how LLMs are constructed and will be familiar with the computational requirements of LLM training and inference. You will learn why GPU hardware is well suited to these workloads and how thousands of GPUs can be interconnected to form an LLM supercomputer. Finally, you will gain insight into the approaches that datacenters use to deploy popular LLMs such as ChatGPT and deliver their capabilities to users around the world.

This chapter will cover the following topics:
* Neural Networks and Large Language Models (LLMs)
* LLM Structure
* LLM Computer Architecture
* Scaling to the Largest LLMs
* Serving LLMs to the World

# Answers to Exercises
The links below lead to the questions and answers for the end-of-chapter exercises.

[Exercise 1](Answers%20to%20Exercises/Ex__1_setup_nanogpt.md): Install nanoGPT and its dependencies, then run it on the prompt “Tell me about GPT-2.”

[Exercise 2](Answers%20to%20Exercises/Ex__2_print_tokens.md): Modify nanoGPT so it prints the tokens and their indices for the prompt “Tell me about GPT-2.”

[Exercise 3](Answers%20to%20Exercises/Ex__3_tile_multiplications.md): Compute the number of tile multiplications and additions involved in multiplying a 1,024 x 768 matrix by a 768 x 768 matrix.

[Exercise 4](Answers%20to%20Exercises/Ex__4_lora_finetuning.md): Apply LoRA fine-tuning to GPT-2 medium and compare its answers to the original model using the same prompts.

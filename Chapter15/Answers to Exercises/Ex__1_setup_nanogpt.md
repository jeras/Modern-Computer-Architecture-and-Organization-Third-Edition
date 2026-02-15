__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 1

Download and install the nanoGPT model from https://github.com/karpathy/nanoGPT. This is an open-source implementation of GPT-2. Install its dependency packages and run it with the prompt “Tell me about GPT-2.”

# Answer
1.	Open a command prompt and change to your project directory, then clone the model repository with the command:
`git clone https://github.com/karpathy/nanoGPT`
1.	Install the required dependencies with this command:
`pip install torch numpy transformers datasets tiktoken wandb tqdm`
1.	Perform inference for the requested prompt with the following command:
`python sample.py --init_from=gpt2 --start="Tell me about GPT-2." --num_samples=5 --max_new_tokens=100`

Some notes regarding the inference command:

* If you do not have a CUDA-capable GPU installed, you will need to modify the line in _sample.py_ that contains `device = 'cuda'` and change it to `device = 'cpu'`.
* It may take some time to download the GPT-2 model weights before inference processing begins.
* GPT-2 does not appear to have been trained with any information about GPT-2, so the five outputs for the given prompt will be nonsense, popularly referred to as hallucinations.

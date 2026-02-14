__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 10: Graphics Processing Units

This chapter examines the architectural and processing details of modern **graphics processing units (GPUs)**. GPUs deliver immense computational power for generating high-resolution 3D scenes in gaming and other video applications, and are essential tools for training and utilizing artificial intelligence models.

We will analyze the computational steps involved in generating video scenes on GPUs, as well as the use of GPUs in machine learning and inference operations for AI applications. This analysis will highlight the potential for improving execution speed by separating computations into many parallel streams in both the video and AI domains.

The discussion continues with a review of the processing architecture of a current-generation GPU, the NVIDIA RTX 3090. We will analyze the board’s hierarchical organization, from the upper-level functions of data distribution and processor scheduling to the lowest level of instruction processing.

We will learn about tensors and their applications in AI. We’ll examine the computations involved in training AI models and the operations required to utilize a trained model for inference, which is the process the model performs when responding to user requests.

After completing this chapter, you will understand the basic architecture of modern GPUs and will be familiar with a modern implementation of GPU technology. You will understand the processing requirements for generating realistic 3D scenes and for training and using neural network models in machine learning applications.

This chapter covers the following topics:
* GPU processing
* GPU hierarchical structure
* Processing clusters and streaming multiprocessors
* GPU memory architecture
* Tensor operations
* Tensor processing

# Answers to Exercises
The links below lead to the questions and answers for the end-of-chapter exercises.

[Exercise 1](Answers%20to%20Exercises/Ex__1_neuron_matrix.md): Formulate the matrix equation that maps hidden-layer neuron outputs to output-layer results.

[Exercise 2](Answers%20to%20Exercises/Ex__2_tiled_matrices.md): Show how two matrix multiplications can be computed in parallel using a tensor core. 

[Exercise 3](Answers%20to%20Exercises/Ex__3_activation_func.md): Compute a neuron’s output using the hyperbolic tangent activation function given the inputs and weights.

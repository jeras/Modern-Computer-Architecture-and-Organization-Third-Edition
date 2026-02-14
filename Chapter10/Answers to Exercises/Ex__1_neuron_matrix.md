__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 10, Exercise 1

Write the matrix computation that transforms the hidden neuron outputs _H_ from _Figure 10.3_ to the results for output neurons _O_. Write out your answer in the same form as Equation 6.7.

# Answer
The equation for computing the results for the output neurons _O_, given the weight matrix _W<sub>HO</sub>_ and the hidden neuron output vector _H_, is as follows:

![Neuron matrix multiplication](Code%20Files/Ex__1_neuron_matrix.png)


The vector elements _WH<sub>1</sub>_ through _WH<sub>3</sub>_ are the result of the multiplication of _W<sub>HO</sub>_ by _H_. Each pass through this computation requires twelve multiplications, nine additions, and three activation function invocations. 
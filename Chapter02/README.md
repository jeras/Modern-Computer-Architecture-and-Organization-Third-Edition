__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 2: Digital Logic

Building upon the topics presented in [Chapter 1, Introducing Computer Architecture](../Chapter01/README.md), this chapter develops a baseline understanding of the digital building blocks used in modern processors and other sophisticated electronic circuits. We begin with a discussion of basic electrical circuit elements and introduce transistors, focusing on their use as switching components in simple logic gates. Next, we construct latches, flip-flops, and ring counters from logic gates. More complex processor components, including registers and adders, are assembled from the devices introduced earlier. The concept of sequential logic, which contains state information that varies over time, will be presented. The chapter concludes with an introduction to hardware description languages, which are the design method of choice for complex digital devices.

The following topics will be covered in this chapter:
* Electrical circuits
* The transistor
* Logic gates
* Latches
* Flip-flops
* Registers
* Adders
* Clocking
* Sequential logic
* Hardware description languages

# Chapter Files
[FullAdder.vhdl](Chapter%20Files/FullAdder.vhdl) is the VHDL implementation of the full adder circuit shown in Figure 2.15.

[Adder4.vhdl](Chapter%20Files/Adder4.vhdl) is the 4-bit adder design in Figure 2.16.

# Answers to Exercises
The links below lead to the questions and answers for the end-of-chapter exercises.

[Exercise 1](Answers%20to%20Exercises/Ex__1_nand_circuit.md): Rearrange the transistor circuit so the AND gate becomes a NAND gate.

[Exercise 2](Answers%20to%20Exercises/Ex__2_or_circuit.md): Create a transistor circuit to implement an OR gate.

[Exercise 3](Answers%20to%20Exercises/Ex__3_vhdl_setup.md): Install a free VHDL suite that includes a simulator and run an example project.

[Exercise 4](Answers%20to%20Exercises/Ex__4_vhdl_project.md): Implement a 4‑bit adder in VHDL.

[Exercise 5](Answers%20to%20Exercises/Ex__5_vhdl_test.md): Write a VHDL test suite that exercises several 4‑bit adder input cases.

[Exercise 6](Answers%20to%20Exercises/Ex__6_vhdl_full_test.md): Extend the test suite to test all possible adder input combinations.

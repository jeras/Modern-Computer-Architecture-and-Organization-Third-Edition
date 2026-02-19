__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 19, Exercise 3

Creates a quantum circuit containing three qubits that implements a **Greenberger–Horne–Zeilinger (GHZ)** state. A GHZ state exhibits strong three-way quantum entanglement: measuring one of the qubits collapses the entire system so that all three qubits yield the same value, no matter how far apart they may be from one another. The correlation appears instantaneously, but no information is transmitted faster than light. In an ideal GHZ state, measurements produce 000b with 50% probability and 111b with 50% probability, with no other outcomes. Execute the code in a simulation environment on your computer.

# Answer
The following program creates the GHZ state and performs 1,024 runs, referred to as _shots_, in a local quantum computer simulator:

[Ex__3_ghz_sim.py](Code%20Files/Ex__3_ghz_sim.py)

This program builds and simulates a three-qubit GHZ state using Qiskit and the Aer simulator (a quantum circuit simulation framework). It performs the following steps:
1.	Constructs a 3-qubit GHZ circuit
2.	Displays a diagram of the circuit
3.	Adds measurements of all three qubits into classical bits
4.	Simulates the circuit on a local AerSimulator backend with 1024 shots
5.	Retrieves the measurement counts
6.	Plots a histogram of measurement results
7.	Analyzes the results, reporting:
* How often 000 and 111 appeared
* How often any unexpected states appeared

This is an example of the output produced by the program:

```
C:\>python Ex__3_ghz_sim.py

Using backend: aer_simulator (local)

Running simulation...

Measurement Results:
{'000': 499, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 525}

Total shots: 1024
Expected states for GHZ: |000⟩ and |111⟩ and no others
|000⟩ observed: 499 times (48.7%)
|111⟩ observed: 525 times (51.3%)
Other states observed: 0 times (0.0%)
```

This is the quantum circuit diagram created by the program: 

![Ex__3_ghz_circuit.png](Code%20Files/Ex__3_ghz_circuit.png)

The following figure presents the program results, showing the number of shots with the 3-bit results 000 and the number with 111, as well as the other possible combinations of measurement outputs:

![Ex__3_ghz_results.png](Code%20Files/Ex__3_ghz_results.png) 
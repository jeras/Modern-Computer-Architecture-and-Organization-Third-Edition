__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 19, Exercise 4

Execute the quantum circuit from [Exercise 3](Ex__3_run_quantum_local.md) on an IBM quantum computer. Due to hardware noise, including gate errors, readout errors, crosstalk, and quantum decoherence, the measurement results will typically include additional bit patterns beyond the ideal outcomes of only 000b and 111b.

# Answer
The following program creates the GHZ state and performs 1,024 shots on an IBM quantum computer:

[Ex__4_ghz.py](Code%20Files/Ex__4_ghz.py)

This Python program constructs a three-qubit GHZ state circuit and runs it on a real IBM Quantum computer using Qiskit Runtime. It performs the following steps:
1.	Builds a 3-qubit GHZ circuit
2.	Displays a diagram of the circuit
3.	Adds measurements of all three qubits into classical bits
4.	Connects to IBM Quantum
5.	Transpiles the circuit for the selected quantum device
6.	Executes the circuit on the quantum hardware
7.	Retrieves the measurement counts
8.	Plots a histogram of measurement results
9.	Analyzes the results, reporting:
* How often 000 and 111 appeared
* How often any unexpected states appeared

This is an example of the output produced by the program:

```
C:\>python Ex__4_ghz.py

Using backend: ibm_fez

Transpiled circuit depth: 9

Submitting job to IBM quantum computer...
Job ID: d4btptvnmdfs73ae954g
Waiting for results...

Measurement Results:
{'000': 484, '001': 2, '010': 6, '011': 12, '100': 7, '101': 7, '110': 4, '111': 502}

Total shots: 1024
Expected states for GHZ: |000⟩ and |111⟩ and no others
|000⟩ observed: 484 times (47.3%)
|111⟩ observed: 502 times (49.0%)
Other states observed: 38 times (3.7%)
```

This is the quantum circuit diagram created by the program, which is the same as in [Exercise 3](Ex__3_run_quantum_local.md):

![Ex__4_ghz_circuit.png](Code%20Files/Ex__4_ghz_circuit.png)

The following figure presents the program results, showing the number of shots with the 3-bit result 000 and the number with 111, as well as the other possible combinations of measurement outputs:

![Ex__4_ghz_results.png](Code%20Files/Ex__4_ghz_results.png)
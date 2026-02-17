#!/usr/bin/env python3

"""Ex__3_ghz_sim.py: Answer to Ch 19 Ex 3."""

from qiskit import (QuantumCircuit, QuantumRegister,
                    ClassicalRegister)
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Create a three-qubit GHZ state circuit
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qr, cr)

# Create GHZ state: |000⟩ + |111⟩ (unnormalized)
circuit.h(qr[0])  # Apply Hadamard to the first qubit
circuit.cx(qr[0], qr[1])  # CNOT from qubit 0 to qubit 1
circuit.cx(qr[0], qr[2])  # CNOT from qubit 0 to qubit 2

# Add measurements
circuit.measure(qr[0], cr[0])
circuit.measure(qr[1], cr[1])
circuit.measure(qr[2], cr[2])

# Display the circuit
circuit.draw(output='mpl')

# Step 2: Set up a local simulator
simulator = AerSimulator()
print(f"\nUsing backend: {simulator.name} (local)")

# Step 3: Run the circuit on the simulator
print("\nRunning simulation...")
job = simulator.run(circuit, shots=1024)

# Step 4: Get results
result = job.result()
counts = result.get_counts(circuit)

# Include 3-qubit combinations with 0 in counts
all_combinations = [
    '000', '001', '010', '011', '100', '101', '110', '111']
counts = {state: counts.get(state, 0) for
          state in all_combinations}

print(f"\nMeasurement Results:")
print(counts)

# Step 5: Plot histogram
plot_histogram(counts)
plt.title("Three-Qubit GHZ State Measurement Results")
plt.tight_layout()
plt.ylim(0, 600)
plt.show()

# Step 6: Analyze results
total_shots = sum(counts.values())
other_states = (total_shots -
                (counts['000'] + counts['111']))
print(f"\nTotal shots: {total_shots}")
print(f"Expected states for GHZ: |000⟩ and " +
      "|111⟩ and no others")
print(f"|000⟩ observed: {counts['000']} times " +
      f"({100 * counts['000'] / total_shots:.1f}%)")
print(f"|111⟩ observed: {counts['111']} times " +
      f"({100 * counts['111'] / total_shots:.1f}%)")
print(f"Other states observed: {other_states} " +
      f"times ({100 * other_states / total_shots:.1f}%)")

#!/usr/bin/env python3

"""Ex__4_ghz.py: Answer to Ch 19 Ex 4."""

from qiskit import (QuantumCircuit, QuantumRegister,
                    ClassicalRegister)
from qiskit_ibm_runtime import (QiskitRuntimeService,
                                SamplerV2 as Sampler)
from qiskit.transpiler.preset_passmanagers \
    import (generate_preset_pass_manager)
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

# Step 2: Set up IBM Quantum service
service = QiskitRuntimeService(
    channel="ibm_quantum_platform")

# Get the least busy backend
backend = service.least_busy(operational=True,
                             simulator=False)
print(f"\nUsing backend: {backend.name}")

# Step 3: Transpile the circuit for the backend
pm = generate_preset_pass_manager(backend=backend,
                                  optimization_level=1)
isa_circuit = pm.run(circuit)

print(f"\nTranspiled circuit depth: {isa_circuit.depth()}")

# Step 4: Run the circuit on IBM quantum hardware
print("\nSubmitting job to IBM quantum computer...")
sampler = Sampler(backend)
job = sampler.run([isa_circuit], shots=1024)

print(f"Job ID: {job.job_id()}")
print("Waiting for results...")

# Step 5: Get results
result = job.result()

# Extract counts from the result
pub_result = result[0]
counts = pub_result.data.c.get_counts()

# Include 3-qubit combinations with 0 in counts
all_combinations = [
    '000', '001', '010', '011', '100', '101', '110', '111']
counts = {state: counts.get(state, 0) for
          state in all_combinations}

print(f"\nMeasurement Results:")
print(counts)

# Step 6: Plot histogram
plot_histogram(counts)
plt.title("Three-Qubit GHZ State Measurement Results")
plt.tight_layout()
plt.ylim(0, 600)
plt.show()

# Step 7: Analyze results
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

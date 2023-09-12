#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:22:30 2023

@author: julio
Qiskit implementation of the Quantum Fourier Transform(QFT) for 3-qubits

"""
import numpy as np
from qiskit import QuantumCircuit

# defines the Quantum circuit for 3 qubits 
qc = QuantumCircuit(3)

# applies the Hadamard gate to the first qubit(qubit 2 in the Qiskit notation)
qc.h(2)

# applies CROT from qubit 1 to qubit 2
qc.cp(np.pi/2, 1, 2)
# applies CROT from qubit 0 to qubit 2
qc.cp(np.pi/4, 0, 2)

# applies the Hadamard gate to the qubit 2, qubit 1 in Qiskit notation
qc.h(1)
# applies CROT from qubit 0 to qubit 1
qc.cp(np.pi/2, 0, 1)

# applies the hadamard on the last qubit, qubit 0 in Qiskit notation
qc.h(0)

# swaps qubit 0 and 2 to account for the sequential implementation of the QFT
qc.swap(0,2)

qc.draw(output='mpl')



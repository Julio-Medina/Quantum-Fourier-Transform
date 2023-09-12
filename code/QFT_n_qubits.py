#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 23:13:32 2023

@author: julio
Qiskit implementation of the general n-qubits Quantum Fourier Transform

"""

import numpy as np
from qiskit import QuantumCircuit#, transpile, Aer, IBMQ
#from qiskit.providers.ibmq import least_busy
#from qiskit.tools.monitor import job_monitor
#from qiskit.visualization import plot_histogram, plot_bloch_multivector


# implements all the operations to the first qubit then the qft_calls it self recursively
# and applies the operation to the next significant qubit until it performs the desired operation 
# on all qubits
def Quantum_Fourier_Transform_unswapped(circuit, n):
    if n == 0: # Exit function if circuit is empty
        return circuit
    n -= 1 # Indexes start from 0
    circuit.h(n) # Apply the H-gate to the most significant qubit
    for qubit in range(n):
        # For each less significant qubit, we need to do a
        # smaller-angled controlled rotation: 
        circuit.cp(np.pi/2**(n-qubit), qubit, n)
    # recursive call of the function Quantum_Fourier_Transform
    Quantum_Fourier_Transform_unswapped(circuit, n)
    
# functions that add the final swapping between qubits
def swap_QFT(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def Quantum_Fourier_Transform(circuit, n):
    # performs all the desired gates to compute the QFT
    Quantum_Fourier_Transform_unswapped(circuit, n)
    # swaps the neccessary qubits at the end, for details check the LaTeX report or Qiskit Textbook
    swap_QFT(circuit, n)
    
    return circuit

n=6 # number of qubits
qc=QuantumCircuit(n) # quantum circuit to compute the QFT on

Quantum_Fourier_Transform(qc, n) # computes the QFT with the function defined above

qc.draw(output='mpl')

        
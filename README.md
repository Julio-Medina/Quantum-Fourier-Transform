# Quantum Fourier Transform

A compact study project on the **Quantum Fourier Transform (QFT)**, developed during graduate-level physics coursework. The repository builds the topic from the classical Fourier series and Fourier transform, then introduces the quantum Fourier transform as a unitary operation on quantum states and implements the corresponding circuit in **Qiskit**.

The project contains both the theoretical report in LaTeX and Python implementations for fixed-size and general QFT circuits.

## Overview

The Quantum Fourier Transform is the quantum analogue of the discrete Fourier transform. For a state

$$
|X\rangle = \sum_{j=0}^{N-1} x_j |j\rangle,
$$

the QFT maps the amplitudes into

$$
|Y\rangle = \sum_{k=0}^{N-1} y_k |k\rangle,
\qquad
 y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j \omega_N^{jk},
$$

where

$$
\omega_N^{jk} = e^{2\pi i jk/N}.
$$

Equivalently, on computational basis states,

$$
|j\rangle \mapsto \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} \omega_N^{jk}|k\rangle.
$$

The QFT is a central primitive in quantum computing, especially in algorithms such as **Shor's factoring algorithm** and **quantum phase estimation**.

## Repository contents

| File | Description |
|---|---|
| `QuantumFourierTransform.tex` | Original LaTeX report written in Spanish. |
| `QFT_3_qubits.py` | Explicit Qiskit implementation of the QFT circuit for three qubits. |
| `QFT_n_qubits.py` | Recursive Qiskit implementation of the QFT circuit for an arbitrary number of qubits. |
| `README.md` | Project overview and usage instructions. |

Optional image files referenced by the LaTeX report, if present in the repository, include QFT circuit diagrams such as `qft_circuit.png`, `qft_3_qubits.png`, and `qft_6_qubits.png`.

## Mathematical background

The report begins with the classical Fourier series representation

$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty} a_n\cos(nx)+\sum_{n=1}^{\infty} b_n\sin(nx),
$$

then moves toward the Fourier integral and the Fourier transform pair

$$
g(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(t)e^{i\omega t}\,dt,
$$

$$
f(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} g(\omega)e^{-i\omega x}\,d\omega.
$$

This classical foundation is then used as motivation for the QFT, which acts on quantum amplitudes instead of directly transforming measured classical data.

## QFT circuit idea

For \(N=2^n\), the QFT circuit can be decomposed into:

1. **Hadamard gates**, which create single-qubit Fourier-basis superpositions.
2. **Controlled phase rotations**, which add relative phases depending on less significant qubits.
3. **Swap gates**, which reverse the output qubit order produced by the sequential circuit construction.

For a computational basis state \(|x\rangle = |x_1x_2\cdots x_n\rangle\), the QFT can be written in product form as

$$
U_{\mathrm{QFT}}|x\rangle =
\frac{1}{\sqrt{N}}\bigotimes_{k=1}^{n}
\left(|0\rangle + e^{2\pi i x/2^k}|1\rangle\right),
$$

up to the usual final qubit-order reversal.

## Python implementation

### Three-qubit QFT

`QFT_3_qubits.py` manually builds the three-qubit circuit using Qiskit:

```python
import numpy as np
from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

qc.h(2)
qc.cp(np.pi/2, 1, 2)
qc.cp(np.pi/4, 0, 2)

qc.h(1)
qc.cp(np.pi/2, 0, 1)

qc.h(0)
qc.swap(0, 2)

qc.draw(output="mpl")
```

### General n-qubit QFT

`QFT_n_qubits.py` implements the same idea recursively. The unswapped QFT applies a Hadamard gate to the most significant remaining qubit, then applies progressively smaller controlled phase rotations. A final swap routine reverses the qubit order.

```python
def Quantum_Fourier_Transform(circuit, n):
    Quantum_Fourier_Transform_unswapped(circuit, n)
    swap_QFT(circuit, n)
    return circuit
```

The default example constructs a six-qubit QFT circuit.

## Installation

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install qiskit matplotlib numpy
```

## Usage

Run the three-qubit implementation:

```bash
python QFT_3_qubits.py
```

Run the general implementation:

```bash
python QFT_n_qubits.py
```

The scripts create Qiskit circuit objects and render them using Matplotlib through `qc.draw(output="mpl")`.

## Suggested improvements

A few useful next steps for the repository would be:

- Add a `requirements.txt` or `pyproject.toml` with the Qiskit dependency.
- Save generated circuit diagrams automatically with `qc.draw(output="mpl").savefig(...)`.
- Add tests comparing the custom QFT circuit with Qiskit's built-in QFT implementation or with the theoretical QFT matrix.
- Refactor function names to follow Python style, for example `quantum_fourier_transform` instead of `Quantum_Fourier_Transform`.
- Add examples that initialize specific basis states and compare the output statevector before and after applying the QFT.

## References

The original report cites standard references including Arfken's *Mathematical Methods for Physicists*, Nielsen and Chuang's *Quantum Computation and Quantum Information*, Mermin's *Quantum Computer Science*, the Qiskit Textbook, and the OpenQASM documentation.

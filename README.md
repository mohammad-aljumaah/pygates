# PyGates

[![PyPI version](https://img.shields.io/pypi/v/pygates-lib.svg)](https://pypi.org/project/pygates-lib/)
![Version](https://img.shields.io/github/v/tag/mohammad-aljumaah/pygates)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#testing)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

A minimal, well-structured Python library for Boolean logic gates, designed for clarity, correctness, and educational use.

---

## License

MIT License

---

## Author

**Mohammad Aljumaah**

https://mohammad-aljumaah.me

https://github.com/mohammad-aljumaah

---

## Overview

`pygates` provides a complete set of Boolean logic operations, including both practical hardware gates and the full set of theoretical 2-input Boolean functions.

The library is designed with a focus on:

* clear API design
* predictable behavior
* strong test coverage
* modular architecture

---

## Installation

### Install from PyPI (recommended)

```bash
pip install pygates-lib
```

---

### Install from GitHub (latest development version)

```bash
pip install git+https://github.com/mohammad-aljumaah/pygates.git
```

---

### Development Installation

Clone the repository:

```bash
git clone https://github.com/mohammad-aljumaah/pygates.git
cd pygates
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install in editable mode:

```bash
pip install -e .
```


---

## Usage

### Basic Operations

```python id="d1k7w4"
from pygates import and_gate, or_gate, not_gate

and_gate(1, 1)   # True
or_gate(0, 1)    # True
not_gate(1)      # False
```

---

### Truth Table Generation

```python id="t5c9r3"
from pygates import print_binary_truth_table, xor_gate

print_binary_truth_table("XOR", xor_gate)
```

---

### Composition

```python id="v2n8x1"
from pygates import and_gate, or_gate, not_gate

A, B, C = True, False, True

result = and_gate(
    or_gate(A, B),
    not_gate(C)
)
```

---

## Available Gates

### Core Gates

| Gate   | Description                        |
| ------ | ---------------------------------- |
| AND    | True if both inputs are True       |
| OR     | True if at least one input is True |
| NOT    | Inverts the input                  |
| XOR    | True if inputs are different       |
| NAND   | Negation of AND                    |
| NOR    | Negation of OR                     |
| XNOR   | True if inputs are equal           |
| BUFFER | Returns the input                  |

---

### Extended Functions

| Function | Description                 |
| -------- | --------------------------- |
| IMPLIES  | Logical implication (A → B) |
| NIMPLIES | Negation of implication     |
| A        | Returns A                   |
| B        | Returns B                   |
| NOT_A    | Negation of A               |
| NOT_B    | Negation of B               |
| TRUE     | Always True                 |
| FALSE    | Always False                |

---

## Testing

Run tests:

```bash id="n2f6q8"
pytest
```

Run with coverage:

```bash id="y4g1t9"
pytest --cov=pygates --cov-report=html
```

Coverage reports are generated in:

```text id="h3z7k5"
htmlcov/index.html
```

---

## Project Structure

```text id="c8w2m6"
pygates/
│
├── src/pygates/
│   ├── gates.py
│   ├── truth_tables.py
│   └── utils.py
│
├── tests/
├── examples.py
└── README.md
```

---

## Use Cases

* Boolean logic learning
* Digital systems education
* Logical expression validation
* Simple circuit modeling
* Teaching and demonstrations

---

## Contributing

Contributions are welcome.

* Open an issue
* Submit a pull request
  
---

## Releases

See: https://github.com/YOUR_USERNAME/pygates/releases

---

## Notes

This project emphasizes:

* clarity over abstraction
* correctness over shortcuts
* simplicity over complexity

---

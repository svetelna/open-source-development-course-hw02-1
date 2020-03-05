# Simple Vector implementation in python 
[![Build Status](https://travis-ci.com/svetelna/open-source-development-course-hw02-1.svg?branch=pr%2Fstep1)](https://travis-ci.com/svetelna/open-source-development-course-hw02-1)
Very simple vector implementation supporting basic operations.

## Usage

```python
from ossdev import Vector, Matrix
a = Vector([0, 1, 2, 3])
print(a)

m = Matrix.ident(4)
print(m)
print(m + m)
```

Operations:
- Addition with a scalar `a+1`
- Vector addition: `a + b`
- Multiplication:
  - scalar * vector
  - row-vector * col-vector
  - col-vector * row-vector
- Vector compare
- Reversion of Vector
- Bitwise xor of Vector with scalar `a^1`

Matrix operations:
- Addition

## Installation

```bash
pip install -U --no-cache . 
```

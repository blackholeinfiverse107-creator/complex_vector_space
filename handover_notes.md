# Handover Notes: Complex Vector Space Module

## Deliverables
1.  **Source Code**: `src/` directory containing `vector_space.py` with `ComplexVector` and `LinearOperator` classes.
2.  **Unit Tests**: `tests/` directory containing deterministic tests for all functionality.
3.  **Documentation**: `mathematical_explanation.md` detailing the theoretical foundations.

## Quick Start

### Prerequisites
- Python 3.6+
- No external dependencies (standard library only).

### Running Tests
Due to the environment issues encountered (Python path), explicit instructions are provided:

1.  Open a terminal in this folder.
2.  Run the tests using your Python executable:
    ```cmd
    "C:\Users\Asus\anaconda3\python.exe" -m unittest discover tests
    ```

### Usage Example
```python
from src.vector_space import ComplexVector, LinearOperator

# Create vectors
v1 = ComplexVector([1, 0])
v2 = ComplexVector([0, 1j])

# Inner product
prod = v1.inner_product(v2)

# Linear Operator (Pauli-Y gate)
Y = LinearOperator([[0, -1j], [1j, 0]])
v_new = Y(v1) # Returns [0, 1j]
```

## Known Issues
- **Environment**: The `python` command may not be in your system PATH. Use the full path to `python.exe` as shown above.

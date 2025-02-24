# Matrix Multiplication Benchmark

This project compares the performance of multi-threading and multi-processing for performing matrix multiplication tasks. It uses Python's `threading` and `multiprocessing` modules to distribute matrix multiplications across multiple workers.

## Features
- Generates large random matrices
- Executes matrix multiplication using both multi-threading and multi-processing
- Measures execution time for both approaches

## Requirements
- Python 3.x
- NumPy

## Installation
Ensure you have Python installed along with NumPy:
```bash
pip install numpy

```

## Configuration
Modify the following parameters in the script to change execution behavior:
- `QUEUE_SIZE`: Maximum queue size for storing tasks
- `MATRIX_SIZE`: Size of the square matrices
- `CALL_RATE`: Time interval between successive tasks
- `TOTAL_CALLS`: Number of matrix multiplication tasks

## Implementation Details
- **Multi-threading:** Uses a `queue.Queue` to distribute matrix multiplication tasks among multiple threads.
- **Multi-processing:** Uses a `multiprocessing.Queue` and `multiprocessing.Process` to execute matrix multiplications in separate processes.
- The script measures and prints the execution time for both approaches.

## Expected Output
The script prints execution times for both multi-threading and multi-processing, allowing users to compare their performance. Typically, multi-processing performs better due to the Global Interpreter Lock (GIL) in Python limiting multi-threading performance.


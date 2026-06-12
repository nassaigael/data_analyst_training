import numpy as np
import time
import random

list_size = 1_000_000

python_array = [random.randint(1, list_size) for _ in range(list_size)]
print("THIS IS THE PYTHON ARRAY")
start_time = time.time()
python_array_sum = sum(python_array)
python_duration = time.time() - start_time
print(f"Python array sum: {python_array_sum}, duration: {python_duration:.6f} seconds")

print("\n" + "=" * 50 + "\n")

numpy_array = np.random.randint(1, list_size, size=list_size)
print("THIS IS THE NUMPY ARRAY")
start_time = time.time()
numpy_array_sum = np.sum(numpy_array)
numpy_duration = time.time() - start_time
print(f"Numpy array sum: {numpy_array_sum}, duration: {numpy_duration:.6f} seconds")

print(
    f"Numpy is {python_duration / numpy_duration:.2f} times faster than Python for summing an array of size {list_size}.")

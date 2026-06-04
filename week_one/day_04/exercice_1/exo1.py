import numpy as np

random_int_array = np.random.randint(1, 1000, 100)

print("Original numpy array")
print(random_int_array)

print(f"\n" + "="*50 + "\n")

min_value = np.min(random_int_array)
max_value = np.max(random_int_array)

normalized = (random_int_array - min_value) / (max_value - min_value)

print(f"Min value on normal array => {min_value} ")
print(f"Max value on normal array => {max_value} ")

print(f"\n" + "="*50 + "\n")
print(normalized)

print(f"\n" + "="*50 + "\n")
print(f" Min value on normalized array => {np.min(normalized)}")
print(f"Max value on normalized array => {np.max(normalized)}")

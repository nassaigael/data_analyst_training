import numpy as np

matrix = np.random.randint(1, 1000, (6, 6))

print("Original Matrix:")
print(matrix)

even_rows = matrix[0:6:2, :]
print("\nRows with even indices:")
print(even_rows)

odd_columns = matrix[:, 1:6:2]
print("\nColumns with odd indices:")
print(odd_columns)

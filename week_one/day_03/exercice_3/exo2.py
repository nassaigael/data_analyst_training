def create_identity_matrix(size):
    """Create an identity matrix of size x size"""
    matrix = []

    for i in range(size):
        row_to_iterate = []
        for j in range(size):
            if i == j:
                row_to_iterate.append(1)
            else:
                row_to_iterate.append(0)
        matrix.append(row_to_iterate)

    return matrix


# Example usage
identity = create_identity_matrix(4)

print("Identity Matrix 4x4:")
for row in identity:
    print(row)

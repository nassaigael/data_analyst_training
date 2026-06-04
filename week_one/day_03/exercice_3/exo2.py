def create_identity_matrix(size):
    """Create an identity matrix of size x size"""
    matrix = []
    
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    return matrix


# Example usage
identity = create_identity_matrix(4)

print("Identity Matrix 4x4:")
for row in identity:
    print(row)
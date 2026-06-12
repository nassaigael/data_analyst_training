import numpy as np


def generate_random_number_array(size=100):
    """Generate a random integer array"""
    array = np.random.randint(1, 1000, size)
    return array


def get_min_and_max(array):
    """Get minimum and maximum values from array"""
    min_value = np.min(array)
    max_value = np.max(array)
    return min_value, max_value


def normalize_array(array):
    """Normalize array between 0 and 1"""
    min_value, max_value = get_min_and_max(array)

    if max_value == min_value:
        print("Eagle: All values are equal")
        return np.zeros_like(array)

    normalized = (array - min_value) / (max_value - min_value)
    return normalized


if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY NORMALIZATION DEMONSTRATION")
    print("=" * 60)

    random_array = generate_random_number_array(100)

    print("\n1. ORIGINAL ARRAY:")
    print(f"   First 10 elements: {random_array[:10]}")

    min_val, max_val = get_min_and_max(random_array)
    print(f"   Min: {min_val}, Max: {max_val}")

    normalized_array = normalize_array(random_array)

    print("\n2. NORMALIZED ARRAY (0 to 1):")
    print(f"   First 10 values: {np.round(normalized_array[:10], 3)}")

    norm_min, norm_max = get_min_and_max(normalized_array)
    print(f"   Min: {norm_min:.6f}, Max: {norm_max:.6f}")

    print("\n3. VERIFICATION:")
    print(f"   Min should be 0: {np.isclose(norm_min, 0)}")
    print(f"   Max should be 1: {np.isclose(norm_max, 1)}")

    print("\n" + "=" * 60)
    print("EDGE CASE: Constant array")
    print("=" * 60)

    constant_arr = np.array([5, 5, 5, 5, 5])
    print(f"Constant array: {constant_arr}")

    normalized_constant = normalize_array(constant_arr)
    print(f"Normalized result: {normalized_constant}")

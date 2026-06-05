import numpy as np

random_int_array = np.random.randint(1, 1000, 100)

def generate_random_number_array(array):
    array = np.random.randint(1, 1000, 100)
    return array

def get_min_and_max(array):
    min_value = np.min(array)
    max_value = np.max(array)
    return min_value, max_value

def normalize_array(array):
    min_value, max_value = get_min_and_max(array)
    
    if max_value == min_value:
        return np.zeros_like(array)
    
    normalized = (array - min_value) /  (max_value - min_value)
    return normalized

# Example usage

if __name__ == "__main__":
    arr = generate_random_number_array(random_int_array)
    print("Example usage (messages in English):")
    print("- Sample of generated numbers:", arr[:10])

    min_val, max_val = get_min_and_max(arr)
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")

    norm = normalize_array(arr)
    print("- Sample of normalized values (first 10):", np.round(norm[:10], 3))
    norm_min, norm_max = get_min_and_max(norm)
    print(f"- Normalized array min: {norm_min}")
    print(f"- Normalized array max: {norm_max}")





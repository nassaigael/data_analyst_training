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






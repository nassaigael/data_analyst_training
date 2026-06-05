import numpy as np

def generate_random_array_with_negative_value(array):
    array = np.random.randint(-100, 100, 100)
    return  array

def replace_all_value_to_zero(array):
    array = np.where( array < 0, 0, array)
    return array

# Example usage
if __name__ == "__main__":
    random_array = generate_random_array_with_negative_value(100)
    
    print("Original (first 10):", random_array[:10])
    print(f"Negatives: {np.sum(random_array < 0)}")
    
    cleaned_array = replace_all_value_to_zero(random_array)
    
    print("Cleaned (first 10):", cleaned_array[:10])
    print(f"Negatives after: {np.sum(cleaned_array < 0)}")
    print(f"All values >= 0: {np.all(cleaned_array >= 0)}")
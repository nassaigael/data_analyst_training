import pandas as pd

def dict_to_dataframe(data_dict):
    if not isinstance(data_dict, dict):
        raise TypeError("Invalid argument: expected a dictionary")
    if not data_dict:
        raise ValueError("Dictionary cannot be empty")
    result = pd.DataFrame(data_dict)
    return result

# Example usage
data = {
    'nom': ['Alice Martin', 'Thomas Dubois', 'Sofia Benali', 'Lucas Bernard', 'Emma Petit'],
    'age': [20, 22, 21, 19, 23],
    'note_math': [15, 12, 18, 14, 11],
    'note_info': [17, 14, 19, 13, 16]
}

df = dict_to_dataframe(data)
print(df)
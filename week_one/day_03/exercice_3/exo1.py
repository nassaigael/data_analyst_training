list_random_number = []

def generate_random_numbers_on_list(list):
    import random
    for i in range(20):
        list.append(random.randint(0, 100))
        
def calculate_mean(list):
    if len(list) == 0:
        return 0
    return sum(list) / len(list)

def calculate_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    
def calculate_std(list):
    if len(list) == 0:
        return 0
    mean = calculate_mean(list)
    variance = sum((x - mean) ** 2 for x in list) / len(list)
    return (variance ** 0.5)


#Example usage:
generate_random_numbers_on_list(list_random_number)
print("Generated List:", list_random_number)
print("length of the list:", len(list_random_number))
print("Mean:", calculate_mean(list_random_number))      
print("Median:", calculate_median(list_random_number))
print(f"Standard Deviation: {calculate_std(list_random_number):.2f}")
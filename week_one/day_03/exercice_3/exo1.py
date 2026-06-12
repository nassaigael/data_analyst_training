import random


def generate_random_numbers_on_list(random_list):
    for i in range(20):
        random_list.append(random.randint(0, 100))


def calculate_mean(random_list):
    if len(random_list) == 0:
        return 0
    return sum(random_list) / len(random_list)


def calculate_median(random_list):
    sorted_list = sorted(random_list)
    n = len(sorted_list)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2


def calculate_std(random_list):
    if len(random_list) == 0:
        return 0
    mean = calculate_mean(random_list)
    variance = sum((x - mean) ** 2 for x in random_list) / len(random_list)
    return variance ** 0.5


# Example usage:
list_random_number = []
generate_random_numbers_on_list(list_random_number)
print("Generated List:", list_random_number)
print("length of the list:", len(list_random_number))
print("Mean:", calculate_mean(list_random_number))
print("Median:", calculate_median(list_random_number))
print(f"Standard Deviation: {calculate_std(list_random_number):.2f}")

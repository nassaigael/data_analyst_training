list_to_test = [12, 15, 8, 1, 14, 7, 16, 1, 13, 10]
result = []

for element in list_to_test:
    if element not in result:
        result.append(element)

print(list_to_test)
print(result)

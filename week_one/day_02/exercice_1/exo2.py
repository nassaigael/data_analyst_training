list = [12, 15, 8, 1, 14, 7, 16, 1, 13, 10]
result  = []

for element in list:
    if element not in result:
        result.append(element)

print(list)
print(result)
a, b = 0, 1
sequence = []

while a < 1000:
    sequence.append(a)
    a, b = b, a + b

print(sequence)

notes = [12, 15, 8, 19, 14, 7, 16, 11, 13, 10]

min_note = notes[0]
max_note = notes[0]
sum_acc = 0
length = 0

for note in notes:
    length += 1
    if note < min_note:
        min_note = note
    if note > max_note:
        max_note = note
    sum_acc += note

average = sum_acc / length

print(f"Minimum note: {min_note}")
print(f"Maximum note: {max_note}")
print(f"Average note: {average:.2f}")

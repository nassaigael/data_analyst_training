age = 1

if age < 0:
    print("Error")
elif 0 <= age < 12:
    print("You are child")
elif 12 < age <= 17:
    print("You are adult")
elif age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

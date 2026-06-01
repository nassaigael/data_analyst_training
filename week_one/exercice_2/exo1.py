age = 1;

if age < 0:
    print("Error")
elif age >= 0 and age < 12:
    print("You are child")
elif age >12 and age <= 17:
    print("You are adult")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
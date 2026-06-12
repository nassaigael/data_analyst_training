annuaire = {
    "Alice": "0612345678",
    "Bob": "0623456789",
    "Charlie": "0634567890"
}

name_to_find = "Alice"
name_to_add = "David"
name_to_remove = "Bob"


def find_phone_number(user_name):
    if user_name in annuaire:
        return annuaire[user_name]
    else:
        return "Name not found in the directory."


def add_phone_number(user_name, number_phone):
    annuaire[user_name] = number_phone
    print(f"{user_name} has been added to the directory with phone number {number_phone}.")


def remove_phone_number(user_name):
    if user_name in annuaire:
        del annuaire[user_name]
        print(f"{user_name} has been removed from the directory.")
    else:
        print("Name not found in the directory.")


find_phone_number(name_to_find)
print(f"The phone number for {name_to_find} is {find_phone_number(name_to_find)}")

add_phone_number(name_to_add, "0645678901")
print(f"The phone number for {name_to_add} is {find_phone_number(name_to_add)}")

remove_phone_number(name_to_remove)
print(f"The phone number for {name_to_remove} is {find_phone_number(name_to_remove)}")

for name, phone_number in annuaire.items():
    print(f"{name}: {phone_number}")

class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if not isinstance(age, int):
        raise InvalidAgeError("Age must be an integer.")
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return "Age is valid."


# Example usage:
try:
    print(validate_age("twenty"))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
try:
    print(validate_age(-5))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
try:
    print(validate_age(150))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
try:
    print(validate_age(25))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

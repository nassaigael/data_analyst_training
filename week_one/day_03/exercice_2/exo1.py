def divide_by_zon_with_exceptions(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."


# Example usage:
print(divide_by_zon_with_exceptions("22", 2))
print(divide_by_zon_with_exceptions(22, 0))
print(divide_by_zon_with_exceptions(22, 2))

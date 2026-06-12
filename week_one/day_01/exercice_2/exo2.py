number = -8;

result = ("positif" if number > 0 else "négatif" if number < 0 else "nul") + " et " + (
    "pair" if number % 2 == 0 else "impair")

print(f"le nombre {number} est {result}")

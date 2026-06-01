poid = 59
taille = 1.75

imc = poid / (taille ** 2)

if imc < 18.5:
    diagnostic = "Underweight"
elif imc >= 18.5 and imc < 25:
    diagnostic = "Normal weight"
elif imc >= 25 and imc < 30:
    diagnostic = "Overweight"
else:
    diagnostic = "Obesity"

print(f"Votre IMC est de {imc:.1f} : {diagnostic}")
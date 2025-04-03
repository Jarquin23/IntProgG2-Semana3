peso_kg = float(input("Ingrese su peso en kilogramos "))
altura = float(input("Ingrese su altura en metros "))
IMC = peso_kg / (altura * altura)
IMC = (IMC * 100) / 100
print("Su peso es de ", peso_kg)
print("Su altura es de ", altura)
print("Su índice de masa corporal es de: ", IMC)
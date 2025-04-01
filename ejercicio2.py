base = float(input("Ingrese la base del rectángulo "))
altura = float(input("Ingrese la altura del rectángulo "))
area = base * altura
perimetro = (base * 2) + (altura * 2)
print(f"El área del rectángulo es: {area: .2f}")
print(f"El perímetro del rectángulo es: {perimetro: .2f}")
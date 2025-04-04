radio = float(input("Ingresar el radio del cilindro "))
altura = float(input("Ingresar la altura del cilindro "))
PI = 3.1416
area_base = PI * (radio * radio)
volumen = area_base * altura
area_lateral = (2 * PI) * (radio * altura)
area_superficial = area_lateral + (area_base * area_base)
print("El radio del cilindro equivale a: ", radio)
print("La altura del cilindro equivale a: ", altura)
print("El volumen tiene un valor de: ", volumen)
print("El área superficial tiene un valor de: ", area_superficial)
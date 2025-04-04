precio_o = float(input("Ingrese el precio del producto "))
desc = float(input("Ingrese el porcentaje de descuento aplicado al producto "))
precio_desc = (precio_o * desc) / 100
desc_final = precio_o - precio_desc
IVA = 0.15
precio_final = (desc_final * IVA)
total = precio_final + desc_final
print("El precio original del producto es de: ", precio_o)
print("El descuento aplicado equivale a: ", precio_desc)
print("El precio con descuento es de: ", desc_final)
print("El valor del IVA calculado es de: ", IVA)
print("El precio final es de: ", total)
s_b = float (input("Ingrese su salario bruto"))
imp_r = (s_b * 0.10)
print("El impuesto sobre la renta es de: ", imp_r)
seg_s = (s_b * 0.5)
print("La cantidad para el seguro es de: ", seg_s)
f_pen = (s_b * 0.3)
print("La cantidad para el fondo de pensión es: ", f_pen)
desc = imp_r + seg_s + f_pen
s_n = s_b - desc
print("Tu salario bruto es: ", s_b)
print("Los descuentos totales equivalen a: ", desc)
print("Tu salario neto es: ", s_n)
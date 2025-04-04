dur_min = float(input("Ingresar la duración de la película en minutos "))
comerciales_prev = float(input("Ingresar la duración de los comerciales previos "))
pausas_com = float(input("Ingresar la cantidad de pausas comerciales durante la película "))
dur_p_com = 10
total_com = pausas_com * dur_p_com
dur_total = (dur_min + comerciales_prev) + pausas_com
print ("La duración original de la película es de: ", dur_min)
print ("La duración total de los comerciales es de: ", total_com)
print ("La duración total de la proyección es de: ", dur_total)
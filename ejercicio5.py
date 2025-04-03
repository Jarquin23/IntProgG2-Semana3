tramo_1 = float(input("Ingrese la duración del primer tramo del vuelo "))
esc_1 = float(input("Ingrese la duración de la primera escala "))
tramo_2 = float(input("Ingrese la duración del segundo tramo del vuelo "))
esc_2 = float(input("Ingrese la duración de la segunda escala "))
tramo_3 = float(input("Ingrese la duración del tercer tramo del vuelo "))
esc_3 = float(input("Ingrese la duración de la tercera escala "))
tp1 = tramo_1 + esc_1
tp2 = tramo_2 + esc_2
tp3 = tramo_3 + esc_3
tiempo_total = tp1 + tp2 + tp3
print("El tiempo total de su vuelo es ", tiempo_total)
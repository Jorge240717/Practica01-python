hora_usuario = input("Ingrese la hora (en formato 24 horas, por ejemplo, 08:30): ")

try:
    horas, minutos = map(int, hora_usuario.split(':'))
    if 7 <= horas <= 8:
        print("Es hora de desayunar.")
    elif 12 <= horas <= 13:
        print("Es hora de almorzar.")
    elif 18 <= horas <= 19:
        print("Es hora de cenar.")
    else:
       pass
except ValueError:
    print("Formato de hora incorrecto. Utilice el formato HH:MM.")


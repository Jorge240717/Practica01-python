try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    opcion = input("Seleccione una opción (1: suma, 2: resta, 3: multiplicación): ")
    if opcion == '1':
        resultado = num1 + num2
    elif opcion == '2':
        resultado = num1 - num2
    elif opcion == '3':
        resultado = num1 * num2
    else:
        raise ValueError("Opción no válida")
    print(f"El resultado es: {resultado}")
except ValueError as e:
    print(f"Error: {e}")



# Solicitar al usuario un entero positivo
N = int(input("Ingrese un entero positivo: "))
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    suma = sum(range(1, N + 1))
print(f"La suma de los enteros desde 1 hasta {N} es: {suma}")
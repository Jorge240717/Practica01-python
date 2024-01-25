costo_comida = float(input("Ingrese el costo de su comida: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))
propina = (porcentaje_propina / 100) * costo_comida
print(f"Debe dejar ${propina:.2f} como propina.")
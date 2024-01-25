lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
indices_a_eliminar = [0, 4, 5]
resultado = [valor for i, valor in enumerate(lista_muestra) if i not in indices_a_eliminar]
print(resultado)

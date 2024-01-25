import mimetypes
def obtener_tipo_mime(nombre_archivo):
    tipo_mime, _ = mimetypes.guess_type(nombre_archivo)
    return tipo_mime if tipo_mime else 'application/octet-stream'
nombre_archivo = input("Ingrese el nombre del archivo: ")
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(f"El tipo MIME del archivo {nombre_archivo} es: {tipo_mime}")
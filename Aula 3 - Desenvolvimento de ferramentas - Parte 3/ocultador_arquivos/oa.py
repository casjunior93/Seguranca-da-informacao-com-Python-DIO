import ctypes

atributos_ocultar = 0X02

retorno = ctypes.cdll.kernel32.SetFileAttributesW("/ocultar.txt", atributos_ocultar)

if retorno:
    print("Arquivo foi ocultado.")
else:
    print("Arquivo não ocultado.")
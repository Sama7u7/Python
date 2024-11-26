def ContarPalabras(texto):
    texto = input("Introduce un texto: ")
    palabras = texto.split() # Separa el texto en palabras
    num_palabras = len(palabras) # Cuenta las palabras
    print(f"El texto tiene {num_palabras} palabras")


ContarPalabras("") 
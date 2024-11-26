import os
from colors1 import colors as c
def CrearDiccionario():
    # Abrir el archivo en modo de escritura, especificando la codificación UTF-8
    with open('diccionario.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("Programar: Es el proceso de crear y ordenar instrucciones para que una computadora las ejecute y realice una tarea específica. Traduccion: Programming\n")  # Escribir en el archivo
        # Puedes seguir escribiendo otras entradas aquí

def leerArchivo():
    with open('diccionario.txt', 'r', encoding='utf-8', errors='replace') as archivo:
        print(archivo.read())  # Leer el archivo y mostrar su contenido

def AgregarPalabra():
    palabra = input('Ingrese la palabra: ')
    significado = input('Ingrese el significado: ')
    traduccion = input('Ingrese la traducción: ')
    with open('diccionario.txt', 'a') as archivo:
        archivo.write(f'{palabra}: {significado}. Traduccion: {traduccion}\n')

def main():
    print('1. Crear diccionario')
    print('2. Leer diccionario')
    print('3. Agregar palabra al diccionario')
    print('4. Eliminar palabra del diccionario')
    print('5. Editar palabra del diccionario')
    print('6. Consultar traduccion de palabra del diccionario')
    print('7. Salir')

    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        CrearDiccionario()
        main()
    elif opcion == 2:
        print('\nDiccionario:')
        leerArchivo()
        main()
    elif opcion == 3:
        AgregarPalabra()
        main()
    elif opcion == 4:
        eliminarPalabra()
        main()
    elif opcion == 5:
        editarPalabra()
        main()
    elif opcion == 6:
        consulta()
    elif opcion == 7:
        exit()
    else:
        print('\nOpción no válida\n')
        main()
main()
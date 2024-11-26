def pagoPorHora():
    horas = int(input('Ingrese las horas trabajadas: '))
    pago = horas * int(input('Ingrese el pago por hora: '))
    print(f'El total de horas trabajadas es: {horas}')
    print(f'El pago total es: {pago}')

def horasTrabajasdas():
    horas = 0
    for i in range(5):
        horas += int(input(f'Ingrese las horas trabajadas el día {i+1}: '))

    print(f'El total de horas trabajadas en la semana es: {horas}')


def main():
    print('1. Pago por horas')
    print('2. Horas trabajadas')
    print('3. Salir')
    
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        pagoPorHora()
        main()
    elif opcion == 2:
        horasTrabajasdas()
        main()
    elif opcion == 3:
        exit()
    else:
        print('Opción no válida')
        main()
main()
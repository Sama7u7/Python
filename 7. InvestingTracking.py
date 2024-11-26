def CalcularInversionTotal():
    # Pedir al usuario los datos de entrada
    inversionInicial = float(input("Ingrese la inversión inicial: "))
    inversionMensual = float(input("Ingrese la inversión mensual: "))
    interesAnual = float(input("Ingrese el interés anual (en porcentaje, ej. 5 para 5%): ")) / 100  # Convertir a decimal
    numeroDeAnos = int(input("Ingrese el número de años: "))  

    # Inicializamos la inversión total con la inversión inicial
    inversionTotal = inversionInicial
    # Convertir el interés anual a mensual
    interesMensual = interesAnual / 12

    # Imprimir encabezados de la tabla
    print("\nMes | Inversión Inicial | Inversión Mensual | Interés Acumulado | Total acumulado")
    print("-" * 80)

    # Empezamos el cálculo mes a mes
    for mes in range(1, numeroDeAnos * 12 + 1):
        # Aplicar el interés mensual a la inversión total
        inversionTotal *= (1 + interesMensual)
        
        # Añadir la inversión mensual después del primer mes
        if mes > 1:
            inversionTotal += inversionMensual

        # Mostrar el estado de la inversión para este mes
        interesAcumulado = inversionTotal - inversionInicial - inversionMensual * mes
        print(f"{mes:3} | {inversionInicial:17.2f} | {inversionMensual:17.2f} | {interesAcumulado:17.2f} | {inversionTotal:16.2f}")

    # Al final, calcular la ganancia total y el interés total
    gananciaTotal = inversionTotal - (inversionInicial + inversionMensual * 12 * numeroDeAnos)
    interesTotal = inversionTotal - (inversionInicial + inversionMensual * 12 * numeroDeAnos)

    # Mostrar resultados finales
    print("\nResultados finales:")
    print(f'La inversión total después de {numeroDeAnos} años es: {inversionTotal:.2f}')
    print(f'La ganancia total es: {gananciaTotal:.2f}')
    print(f'El interés total ganado es: {interesTotal:.2f}')

# Llamar a la función para calcular la inversión
CalcularInversionTotal()

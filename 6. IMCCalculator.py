def IMC():
    peso = float(input("Digite su peso: "))
    altura = float(input("Digite su altura: "))
    imc = peso / (altura ** 2)
    print(f"Su Indice de Masa Corporal IMC es: {imc:.2f}")
    if imc < 18.5:
        print("Usted esta bajo de su peso ideal")
    elif imc < 25:
        print(" Usted esta en su peso normal")
    elif imc < 30:
        print("Usted tiene sobrepeso")
    elif imc < 35:
        print("Usted tiene obesidad grado 1")
    elif imc < 40:
        print("Usted tiene obesidad grado 2")
    else:
        print("Usted tiene obesidad grado 3")

IMC()
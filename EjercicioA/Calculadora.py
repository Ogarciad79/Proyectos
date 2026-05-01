while True:
    texto1 = input('Ingresa el primer valor (o "salir"): ').strip()
    if texto1.lower() == "salir":
        break

    texto2 = input('Ingresa el segundo valor (o "salir"): ').strip()
    if texto2.lower() == "salir":
        break

    try:
        num1 = float(texto1)
        num2 = float(texto2)
    except ValueError:
        print('Entrada inválida. Escribe un número o "salir".')
        continue

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 == 0:
        division = None
    else:
        division = num1 / num2

    print("La suma de los dos numeros es:", suma)
    print("La resta de los dos numeros es:", resta)
    print("La multiplicacion de los dos numeros es:", multiplicacion)
    if division is None:
        print("La division de los dos numeros es: indefinida (división entre 0)")
    else:
        print("La division de los dos numeros es:", division)
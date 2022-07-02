#funcion y ciclo

def funcion(numero1, numero2):
    if (numero1 == numero2):
        print("los numeros son iguales")
    elif (numero1 > numero2):
        print("el numero " + str(numero1) + " es mayor que el numero " + str(numero2))
    else:
        print("el numero " + str(numero2) + " es mayor que el numero " + str(numero1))


funcion(5,6)

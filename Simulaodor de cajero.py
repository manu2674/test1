# Simulador de cajero; ejercicio pedido a chatgpt, *para recordar y traabajar un poco mas

# Condiciones:

# Empiezas con un saldo, por ejemplo 1000 €.
# El menú se repite hasta elegir 4.
# Al ingresar dinero, aumenta el saldo.
# Al retirar, comprueba que tengas suficiente dinero.
# No permitas ingresar o retirar cantidades negativas.

# EXTRA MIO, Le añadi un numero random si lo pones en el menu se hackea y te da 1 millon.

# Menu
import random 
menu = -1
saldo=1000
# Chatgpt me corrigio porque el ramdon lo puse en el elif del "hack" y cada vez de reiniciaba, dandole una variable no; no cai jaja
numero_secreto = random.randint(5, 10)
print(f"Modo Prueba el numero para hackear el cajero es: {numero_secreto}")
    #menu=int(input("       \033[35mCajero\033[0m\n\n\033[36m1. Consulta dinero\033[0m\n\033[32m2. Ingresa dienro\033[0m\n\033[35m3. Retira dienro\033[0m\n\033[31m0. Salir\033[0m\n\nEligue una opción: "))
while menu != 4:
    menu=int(input("       Cajero\n\n1. Consulta dinero\n2. Ingresa dienro\n3. Retira dienro\n4. Salir\nEligue una opción: "))
    if menu == 1:
        #Comprobar el saldo
        print(f"El Saldo acutal es {saldo}€\n")
    elif menu == 2:
    # Pide cuanto quiere ingresar y lo suma al saldo
        ingreso=int(input("Introduzca el ingreso a realizar: "))
        saldo=saldo+ingreso
        print(f"Ingreso de {ingreso}€ realizado\n")
    elif menu == 3:
    # Pide cuanto quiere retirar
        retiro=int(input("Introduzca el retiro a realizar: "))
        # Comprueba que el retiro se puede realizar
        if retiro <= saldo:
            # Si el retiro se puede llegar a cabo se resta del saldo 
            saldo=saldo-retiro
            print(f"Retiro de {retiro}€ realizado\n")
        # Y si no hay suficiente saldo, deniega el retiro
        else:
            print(f"\033[31mNo se puede retirar más dinero que el saldo: {saldo}\033[31m\n")
        #Si adivinas el numero secreto el sistema se hackea y recibes 1 millon
    elif menu == numero_secreto:
        saldo=saldo+1000000
        print(f"\033[33mcajero hackeado su saldo actual asciende a {saldo}€\033[0m \n")
    elif menu == 4:
        print("\nGracias por utilizar el cajero.")
    else:
        print("\033[31mOpción no válida\033[0m\n")

















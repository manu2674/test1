# calcular area o longitud
import math
letra=str(input("Dame una letra: ")).upper()
radio=int(input("Dame un radio: "))
if letra == "A":
    area=math.pi*radio**2
    print(F"El area es {area}")
elif letra == "L":
    longitud=2*math.pi*radio
    print(F"El longitud es {longitud}")
else:
    print("Letra no valida")
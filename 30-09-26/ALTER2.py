# Pide 2 numeros y muestra antes el mayor y luego el menor
numero1=int(input("Dame un nuemro: "))
numero2=int(input("Dame otro nuemro: "))
if numero1 > numero2:
    mayor=numero1
    menor=numero2
else:
    mayor=numero2
    menor=numero1

print(f"E mayor es {numero1} ")
print(f"El menor es {numero2}")
# Calcular si es equilátero, isósceles o escaleno.
num1=int(input("Dame un lado 1: "))
num2=int(input("Dame un lado 2: "))
num3=int(input("Dame un lado 3: "))

if num1==num2==num3:
    print("EQUILATERO")
elif num1==num2 or num2==num3 or num1==num3:
    print("ISOSCELES")
else:
    print("ESCALENO")
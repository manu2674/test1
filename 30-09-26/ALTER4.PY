# DECIR SI ES VOCAL O CONSONATE
letra=str(input("Dame una letra: ")).lower()
if letra in "aeiou":
    print("Es una vocal")
else:
    print("Es una consonate")
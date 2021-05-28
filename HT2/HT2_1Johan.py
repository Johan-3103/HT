entero = int(input ("Escriba un número entero positivo:  "))
while entero <= 0:
    entero = int(input ("Escriba un número entero mayor a 0:  "))

if entero > 0:
     for i in range(entero):
        for j in range(i+1):
            print("*", end="")
        print("")

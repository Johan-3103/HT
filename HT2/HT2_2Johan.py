entero = int(input ("Escriba un número entero positivo:  "))
while entero <= 0:
    entero = int(input ("Escriba un número entero mayor a 0:  "))
for i in range (entero+1):
    print (entero-i,end=", ")

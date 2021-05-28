entero = int(input ("Escriba un número entero  mayor a 2:  "))
while entero <= 2:
    entero = int(input ("Escriba un número entero mayor a 2:  "))
i=2
while entero % i != 0:
    i= i+1
if i== entero :
    print (str(entero)+" es primo") 
else:
    print (str(entero)+" no es primo")
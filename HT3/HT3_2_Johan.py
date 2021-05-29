nombre = input ("¿Cómo te llamas?  ")
sexo = input ("¿Cuál es tu sexo? (M ó H) : ")
Hombre = ("H")
Mujer = ("M")

if sexo == Mujer.lower():
    if nombre.lower() < "m" :
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n" :
        grupo = "A"
    else:
        grupo = "B"
print ("tu grupo es: "+ grupo)
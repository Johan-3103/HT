contra = input ("Escriba su contraseña: ")
contra_user = input ("Confirme su contraseña: ")
while contra_user.lower() != contra.lower() :
    contra_user = input ("Su contraseña no coincide, intente nuevamente: ")
if contra_user.lower() == contra.lower() :
    print("Su contraseña es correcta, Bienvenido ")


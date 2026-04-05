# verificador de contraseña simple

password = input("Ingresa una contraseña: ")

if len(password) < 6:
    print("Contraseña débil")
else:
    print("Contraseña aceptable")

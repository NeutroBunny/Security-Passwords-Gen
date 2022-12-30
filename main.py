import random

chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&(`)_/{}"

while 1:
  password_len = int(
    input("¿Qué longitud le gustaría que tuviera su contraseña?: ")
  )  #Longitud de la contraseña
  password_count = int(
    input("Cuantas contraseñas quieres: "))  #Numero de contraseñas
  for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
      password_char = random.choice(chars)
      password = password + password_char
      
    print("Aquí está tu contraseña: ",)
    print(password)
    print("Contraseñas hechas con Gen Password, Hecho por: Neutro Bunny")
print("")
    #Contraseña Generada

#Hecho por: Neutro Bunny

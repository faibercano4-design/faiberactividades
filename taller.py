def saludar(nombre):
    print("hola mundo", nombre)



for numero in range(1,13):
    print(numero)
    print("---------------")
    nombre = input("ingrese su nombre: ")
    if nombre.lower().strip() == "salir":
       break
    saludar(nombre)

while(True):
    print("Aqui inicia el while")
    nombre = input("ingrese su  nombre") 
    
    # lower() pasar a minusculas
    #strinp() pasar mayuscula
    if nombre.lower().strip() == "salir":
       break
    
    saludar(nombre) 

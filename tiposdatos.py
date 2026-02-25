listaTest = [1, 2, "Hola mundo", 0.9, True] #Lista
tuplaTest = (1,2,3) #Tupla, no se puede modificar 
diccionario = {"Nombre": "Camilo",
               "Edad":20,         #Diccionario
               "Correo": "test@test.com"}

print(listaTest[3]) #Hola mundo
print(tuplaTest[2]) #3
print(diccionario["Edad"]) #20

print("Imprimiendo Lista")
for i in listaTest:
    print(i)

    print("-------------Imprimiendo Tupla---------------")
    for i in tuplaTest:
        print(i)



    print("------------Inprimir Diccionario------------------")
    for clave, valor in diccionario.items():
        print(f"Esta es la clave {clave} y este el valor {valor}")

    print ("--------------Imprimir lista con WHILE---------------------")
    tamañolista = len(listaTest)
    contador = 0 
    while(contador < tamañolista ):
        print(listaTest[contador])
        contador += 1


    print ("--------------Imprimir Tupla con WHILE---------------------")
    tamañolista = len(tuplaTest)
    contador = 0 
    while(contador < tamañolista ):
        print(tuplaTest[contador])
        contador += 1

    print ("--------------Imprimir Diccionario con WHILE---------------------")
    claves = list(diccionario.keys())
    lenClaves = len(claves)
    i = 0 
    while(i < lenClaves):
        print("Esta es mi clave: ", claves[i])
        print(f"Este es el valor:{diccionario[claves[i]]}")
        i += 1

    print("---------Convirtiendo texto a lista------------------")
    texto = "Hola mundo"
    print(list(texto))


    print("------Trabajo con listas----------")
    frutas = ["pera","Manzana", "Fresas", "Banana", "Uva"]
    print(frutas[2]) #Fresas
    print(frutas[0:2]) #[´Pera´,'Manzana']
    print(frutas[-1]) #Uva
    print(frutas[-1:])#['Uva']
    print(frutas[:-1])#[´pera´, 'Manzana´,´Fresas´,´Banana´]
    print(frutas[::2]) #['Pera´,´Fresas´,´Uva´] Cada 2 elementos

    frutas.pop() #Quita el ultimo elemento
    print("Quitamos un elemento")
    print(frutas)
    print("Agregamos un elemento")
    frutas.append("Mora")
    print(frutas)
    frutas.pop(1) #Quita el elemento por posicion 
    print(frutas)
    print("Quito elemntos por mombre")
    frutas.remove("Fresas")
    print(frutas)
    print("Agregar elemento por pocision")
    frutas.insert(2,"Cereza")
    print(frutas)
    print("Modificar elemento por posicion")
    frutas[1] = "kiwi"
    print(frutas)
    print("Ver lista al reves")
    print(frutas[::-1])
    frutas.reverse() #Modifica la lista
    print(frutas)
    frutas = reversed(frutas) #Invierte un objeto
    print(list(frutas))
    texto2 = "".join(reversed(texto)) #Convierte un objeto -> str
    print(texto2, texto)

    frutas2 = frutas
    #frutas2
    frutas = (list(frutas2))
    frutas.append("pera")
    print(frutas2, frutas)
    """---Diccionario--"""
    print("--diccionario---")
    print (diccionario["Edad"])
    diccionario["Direccion"] = "Av caracas"
    print(diccionario)
    diccionario["Edad"] = [20, 30]
    print(diccionario)
    diccionario ["Edad"] = 30
    print(diccionario)
    print(diccionario.get("telefono", "esta clave no existe"))
def main():
    print("INICIO PROGRAMA")
    producto = {}

    nombre = input("Ingrese el nombre del producto:\n")
    precio = float(input("ingrese el precio:\n"))
    cantidad = int(input("Ingrese la cantidad\n"))

    producto["nombre"] = nombre
    producto["precio"] = precio
    producto["cantidad"] = cantidad
    print("El diccionario es:", producto)
    print("FInalizo el programa")  
    

if __name__ == "__main__":
    main() 

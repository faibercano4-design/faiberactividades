def menu():
    print("---MENU---")
    print("---Bienvenido por favor ingrese una opcion: ")
    opciones = """ 1) agregar productos
                  2) ver inventario
                  3) consultar
                  4) salir  
    """
    print(opciones)

def main():
    
    inventraio = [] #guardar los productos
    while(True): 
       menu()
       opcion = int(input("Seleccione una opcion:\n"))
       
       if opcion == 1:
           print("Nuevo producto")
           nombre = input("Ingrese el nombre: ")
           precio = float(input("Ingrese el precio: "))
           cantidad = int (input("Ingrese la cantidad: "))
           producto = {"Nombre": nombre,
                       "precio": precio}
           producto["cantidad"] = cantidad

           inventraio.append(producto)
           print("producto guardada con exito")

       elif opcion == 2:
           print("inventario actual")

           if len(inventraio) == 0:
               print("inventario vacio")
           else:
             for item in inventraio: 
                print(f"nombre del producto{item["nombre"]}\
                      y el precio es {item["precio"]}\
                        cantidad es {item["cantidad"]}")            
          
       elif opcion == 3:
           pass
       elif opcion == 4:
           pass
       else:
           print("opcion no valida")



if __name__ =="__main__":
   main() 
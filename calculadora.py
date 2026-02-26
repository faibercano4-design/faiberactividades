#calculadora

def suma(valor1, valor2, parametro):
    resultado = 0
    resultado = valor1 + valor2
    print("resultado de la suma", resultado)
    #esta funcion va sumar los valores (+)


def multiplicar(valor1, valor2, parametro):
    resultado = 0
    resultado = valor1 * valor2
    print("resultado de la multiplicacion", resultado)
    #esta funcion va multiplicar los valores (*)


resultado= 0

def resta(valor1, valor2, parametro):
    resultado = 0
    resultado = valor1 - valor2
    print("resultado de la resta", resultado)
    #esta funcion va rrestar los valores     (-)


def dividir(valor1, valor2, parametro):
     resultado = 0
     resultado = valor1 / valor2
     print("resultado de la division", resultado)
     #esta funcion va a dividir los valores  (/)


numero1 = 0
numero2 = 0

mensaje = """por favor ingresar la operacion que quiera realizar
              1) sumar
              2) restar
              3) multiplicar
              4) dividir
           """
operacion_usuarrio = 0
operacion_usuario=  int(input(mensaje)) 

numero1 = int(input("ingrese el valor 1:"))
numero2 = int(input("ingrese el valor 2:"))

if operacion_usuario == 1:
 suma(numero1, numero2)   

elif operacion_usuario == 3:
 multiplicar(numero1, numero2)

elif operacion_usuario == 2:
   resta(numero1, numero2)

elif operacion_usuario == 4:
   dividir(numero1, numero2)
else:
     print("la opcion ingresada no es valida") 
    


 






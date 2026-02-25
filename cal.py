#función para calcular
def calcular(valor1, valor2, parametro):

    resultado = 0
    if parametro == "+":
        resultado = valor1 + valor2
    elif parametro == "-":
        resultado = valor1 - valor2
    elif parametro == "*":
        resultado = valor1 * valor2
    elif parametro == "/":
        resultado = valor1 / valor2

    else:
        print("el parametro ingresado no es valido.")
        #return "SI"
       
    print("El resultado de la operacion es: ", resultado)
    #return "OK"
numero1 = 0
numero2 = 0
parametro = ""



mensaje ="""
ingrese el simbolo de la operación que quirera realizar:
sumar: +
restar: -
multiplicar: *
dividir: /
"""

#variable_salida = "SI"

""" while(variable_salida != "OK"):
    parametro = input (mensaje)
    variable_salida = calcular(numero1, numero2, parametro) """

for i in range(1,5):
    numero1 = int(input("ingrese un numero:"))
    numero2 = int(input("ingrese el segundo numero a operar"))
    parametro = input (mensaje)
    
    calcular(numero1, numero2, parametro)




        
                      

#Tablas de verdad
print("---tablas de verdad-----")    

A = True
B = False
C = True

if A and B:
    print("verdadero")
elif A and B or C:
     print("segunda opcion")
else:
    print("falso")

print("---Banco-----")    

edad = 0 # cero,none,""
ingresos = 0
reporte = ""
fiador = ""

edad = int(input("Ingrese su edad:\n"))
ingresos = float(input("ingrese sus ingresos mensuales:\n"))

fiador = input("Tiene fiador?: (SI/NO):\n")
reporte = input("Esta usted reportado?: (SI/NO):\n").upper()

tieneEdad = (edad >= 18 and edad < 75)
#ingresos = ( ingresos >= 2000000.0)

tieneFiador = None 

if fiador.upper() == "SI" or ingresos >= 2000000.0:
    tieneFiador = True
else:    
    tieneFiador = False 

tieneReporte = (reporte == "SI")

creditoAprobado = tieneFiador and tieneReporte and tieneEdad

if creditoAprobado:
    creditoAprobado = "felicitaciones"
else:
    creditoAprobado = "lo sentimos"    

print("edad:", tieneEdad)
print("fiador o ingresos:", tieneFiador)
print("reporte:", tieneReporte)
print (f"estado de su credito: {creditoAprobado}. :)")
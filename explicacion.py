def main():
    print("INICIO EL PROGRAMA")
    notas = []

    try:
        for i in range(1,4):
            print("Paso", i)
            nota = float(input("Ingrese la nota:\n"))
            notas.append(nota)
            if nota < 3.0:
                print("Reprobo",)
            elif nota < 4.0:
                print("Aceptable")
            else:
                print("Exelente")

        print("Estas son las notas", notas)     
        temanolista = len(notas)
        contador = 0
        sumaNotas = 0
        while(contador < temanolista):
            notaWhile = notas[contador]
            sumaNotas += notaWhile
            contador += contador + 1
        promedio = sumaNotas/temanolista
        print("Su promedio es:", sumaNotas/temanolista) 
    #  except ValueError:
    #      print("falle por tipo de datos")
    except Exception as e: 
        print("El programa fallo por otro problema.")
    finally:
        print("El programa finalizo")

if __name__ == "__main__":
   main() 
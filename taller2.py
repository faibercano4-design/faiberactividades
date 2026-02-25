def notas(nota):

    if nota >= 40 and nota <= 50:
        print("Excelente")
    elif nota >= 30 and nota <= 39:
        print("Sobresaliente") 
    elif  nota <= 29 and nota >= 0: 
        print("Reprobo")   
    else:
        print("Reprobo") 
nota = int (input("ingrese la nota\n"))        

notas(29)              
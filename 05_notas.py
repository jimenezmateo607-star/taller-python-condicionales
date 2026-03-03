while True:
    try:
        nota1=float(input("Ingrese su primera calificación: "))
        while nota1 >100 or nota1<0:
            print("Introduce notas entre 0 y 100")
            nota1=float(input("Ingrese su primera calificación: "))
        nota2=float(input("Ingrese su segunda calificación: "))
        while nota2 >100 or nota2<0:
            print("Introduce notas entre 0 y 100")
            nota2=float(input("Ingrese su segunda calificación: "))
        nota3=float(input("Ingrese su tercera calificación: "))
        while nota3 >100 or nota3<0:
            print("Introduce notas entre 0 y 100")
            nota3=float(input("Ingrese su tercera calificación: "))
        break
    except:
        print("Introduce un número valido por favor")

prom=((nota1+nota2+nota3)/3)
if prom >= 90:
    coment=("Excelente")
elif prom >= 80:
    coment=("Muy bueno")
elif prom >= 70:
    coment=("Bueno")
elif prom >= 60:
    coment=("Supletorio")
else:
    coment=("reprobado")

print("\n-NOTAS-\n")
print(f"Tu primera nota fue {nota1}")
print(f"Tu segunda nota fue {nota2}")
print(f"Tu tercera nota fue {nota3}")
print(f"Tu promedio es {prom}")
print(f"Tu clasificación final es {coment}")




while True:
    try:
        número=float(input("Dame un número: "))
        if número%2 == 0:
            print(f"El número {número} es par")
            break
        else:
            print(f"El número {número} es impar")
            break
    except:
        print("introduce un número valido por favor.")
while True:
    try:
        edad=float(input("Dame tu edad: "))
        if edad >= 18:
            print("Eres mayor de edad")
            break
        else:
            print("No eres mayor de edad")
            break
    except:
        print("Introduce un número válido por favor")






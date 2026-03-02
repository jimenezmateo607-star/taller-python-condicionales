print("¡¡¡Un saludo usuario!!!")
while True:
    try:
        km=float(input("¿Cuántos kilómetros recorriste?: "))
        break
    except:
        print("Introduce un número por favor")


try:
    hora=int(input("¿A qué hora viajaste?"))
    while hora >23 or hora < 0:
        print("Introduce un valor entero entre 0 y 23 por favor")         
        hora=int(input("¿A qué hora viajaste?:  "))    
except:
        print("Introduce un valor entero entre 0 y 23 por favor")

if hora > 5 and hora < 20:
    costo_por_km=0.5
if hora > 19 or hora < 6:
    costo_por_km=0.65

if km <= 10:
    Precio=1+(km*costo_por_km)
else:
    precio=2+(km*costo_por_km)
print(f"El costo de tu viaje es {precio:,.2f}$")




while True:
    try:
        subtotal=float(input("Cuál fue tu subtotal?: "))
        break  
    except:
        print("Introduce un valor válido")

tipo_cliente=input("Eres cliente vip o regular)?: ")
while tipo_cliente!="vip" and tipo_cliente!="regular":
    print("Introduce un valor adecuado (vip/regular)")
    tipo_cliente=input("Eres cliente vip o regular)?: ")

if tipo_cliente == "vip": 
    Descuento=0.15
elif subtotal >= 100:
    Descuento=0.05
total=subtotal-(subtotal*Descuento)
print(f"\n-TICKET-\n")
print(f"Tu subtotal es {subtotal}")
print(f"Tu descuento aplicado es de {Descuento}%")
print(f"Tu total es {total}")



            

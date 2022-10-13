numero=int(input("Digite el numero al que desea aplicarle el factorial: "))
total=1
for i in range (1,numero+1):
    total=total * i

print("\nEl factorial del numero " + str(numero) + " es " + str(total))
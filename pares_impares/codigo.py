cantpares=0
cantimpares=0

for i in range(1,100):
    num=int(input("Digite un numero: "))
    if num%2 == 1:
        cantimpares=cantimpares +1 
    else:
        cantpares=cantpares + 1

print("\nLa cantidad de pares es " + str(cantpares) + ", y la cantidad de impares es " + str(cantimpares))

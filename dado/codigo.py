from random import random


import random
n=int(input("Cuantos dados vas a lanzar?: "))

cant1=""
cant2=""
cant3=""
cant4=""
cant5=""
cant6=""


for i in range (1,n+1):
    lanzamiento=int(random.uniform(1,7))
    if lanzamiento==1:
        cant1=cant1 + "*"

    elif lanzamiento==2:
        cant2=cant2 + "*"

    elif lanzamiento==3:
        cant3=cant3 + "*"

    elif lanzamiento==4:
        cant4=cant4 + "*"

    elif lanzamiento==5:
        cant5=cant5 + "*"

    elif lanzamiento==6:
        cant6=cant6 + "*"

print("\n1: " + str(cant1))
print("2: " + str(cant2))
print("3: " + str(cant3))
print("4: " + str(cant4))
print("5: " + str(cant5))
print("6: " + str(cant6))



multi9=0
multi7=0
for i in range(1000, 5001):
    if i%7==0:
        multi7=multi7+1
    if i%9==0:
        multi9=multi9+1
    
print("\nLa cantidad de multiplos de 7 es " + str(multi7) + " y la cantidad de multiplos de 9 es " + str(multi9))
#MARIO RODRÍGUEZ 

#Primer ejercicio
print("Programa que lea 100 números enteros y escriba la suma de todos ellos.")
n = 100
sumat = 0

while n > 0:
    num = int(input("Número: "))
    sumat = sumat + num
    n = n-1

print ("La suma de los números digitados es: ", sumat)
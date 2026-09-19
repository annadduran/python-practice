from math import sqrt

a = int(input("Ingresa un valor para a: "))
b = int(input("Ingresa un valor para b: "))
c = int(input("Ingresa un valor para c: "))
x1 = 0 
x2 = 0

if ((b**2) - (4* a * c)) < 0:
    print("No se puede realizar porque no se puede sacar raiz cuadrada de un número negativo")
else:
    x1 = (-b + sqrt((b**2 )- (4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2 )- (4*a*c))) / (2*a)
   
print("La solución es:  \nx1=", x1, "\nx2=", x2)
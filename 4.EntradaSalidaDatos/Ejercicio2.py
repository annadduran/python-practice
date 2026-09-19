p1 = float(input("Ingresa un valor para practica uno: "))
p2 = float(input("Ingresa un valor para practica dos: "))
p3 = float(input("Ingresa un valor para practica tres: "))
ep = float(input("Ingresa un valor para examen parcial: "))
ef = float(input("Ingresa un valor para examen final: "))

pp = ( p1 + p2 + p3 ) / 3
prom = ( pp + 2 * ep + 3 * ef ) / 6
print("El promedio de practica es de:\n", pp, "\n y el promedio final es de: \n", prom )
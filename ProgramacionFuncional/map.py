#map high order example 
def celsius2far(temp):
    return (temp * 9 / 5) + 32

temps = [0, 20, 30, 100]

new_temps = list(map(celsius2far, temps))

#aplicar una funcion a cada elemento en una entrada iterable
 
import math

# Suma de los cuadrados de los primeros 100 números naturales

f = 0
suma = 0
while f <= 100:
    suma += f**2
    f += 1
print (f"La suma de los primeros 100 números naturales al cuadrado es: {suma}")

# Se lee un entero desde el teclado y se suman los 100 números siguientes

print("Suma de los 100 números siguientes")
d = int(input("Ingrese un número entero "))
suma = 0
for i in range(d+1, d+101):
    suma += i
print (f"La suma de los siguientes 100 números después del ingresado es: {suma}")

# Euros a dólares

print("Convertir euros a dólares")
euro = float(input("Ingrese el valor en euros que quiere convertir a dólares "))
while euro:
    conversión = euro * 1.13
    break
print(f"{euro} euros son {conversión:.3f} dólares")  #.3f para que solo se muestre el resultado con 3 decimales

# Área de un rectángulo

print("Conocer el área de un retángulo")
alto = float(input("Ingrese la altura del rectángulo "))
ancho = float(input("Ingrese el ancho del rectángulo "))
while alto and ancho:
    area = alto * ancho
    break
print(f"El área del rectángulo es {area:.3f}")

# Número mayor y número menor

print("Saber cuál número es mayor y cuál es menor")
n1 = int(input("Ingrese un número "))
n2 = int(input("Ingrese otro número "))
while n1 and n2:
    if n1>n2:
        print(f"{n1} es el número mayor")
        print(f"{n2} es el número menor")
    else:
        print(f"{n1} es el número menor")
        print(f"{n2} es el número mayor")
    break

# Números impares menores que el numero ingresado

print("Números impares menores que un número")
x = int(input("Ingrese un número "))
print(f"Los números impares menores que {x} son")
for i in range(1, x):
    if i % 2 == 1:
        print(i)

# Algoritmo de Euclides para encontrar el MCD de dos números

print("Máximo común divisor de dos números")
mayor = int(input("Ingrese el número mayor "))
menor = int(input("Ingrese el número menor "))
while menor != 0:
    residuo = mayor % menor
    mayor = menor
    menor = residuo
print(f"El máximo común divisor de ambos números es {mayor}")

# Solución de ecuación cuadrática

print("Solución para una ecuación cuadrática: ax² + bx + c")
a = int(input("Ingrese un valor para a "))
b = int(input("Ingrese un valor para b "))
c = int(input("Ingrese un valor para c "))
raiz = int((b**2)-4*a*c)
if raiz <0:
    print("Esta ecuación no tiene solución")
elif raiz == 0:
    x = -b/(2*a)
    print(f"Esta ecuación tiene una única solución: x = {x}")
else:
    x1 = (-b - raiz)/2*a
    x2 = (-b + raiz)/2*a
    print(f"Esta ecuación tiene dos soluciones x1 = {x1} y x2 = {x2}")





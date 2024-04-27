
#-----------------------------
#Conjuntos de datos
#-----------------------------
# Definir una lista
mi_lista = ["manzana", "banana", "cereza"]

# Definir una tupla
mi_tupla = ("manzana", "banana", "cereza")

# Definir un diccionario
mi_diccionario = {"nombre": "Juan",
                   "edad": 25, 
                   "ciudad": "Madrid"}

# Definir un conjunto
mi_conjunto = {"manzana", "banana", "cereza"}

#-----------------------------
# Operadores
#-----------------------------
x = 6 ; y = 2
print(x + y)  # Suma
# Output: 8
print(x - y)  # Resta
# Output: 4
print(x * y)  # Multiplicación
# Output: 12
print(x / y)  # División
# Output: 3
print(x % y)  # Módulo
# Output: 2
print(x ** y) # Potencia
# Output: 36
print(x // y) # División entera
# Output: 3

x = 5 ; y = 3
print(x == y)  # Igual a
print(x != y)  # Distinto a
print(x > y)   # Mayor que
print(x < y)   # Menor que
print(x >= y)  # Mayor o igual que
print(x <= y)  # Menor o igual que

print(x > 3 and x < 10)  # Ambas condiciones deben ser verdadera
s
print(x > 3 or x < 4)    # Al menos una condición debe ser verda
dera
print(not(x > 3 and x < 10))  # Invierte el resultado

#-----------------------------
#Cadenas de caracteres
#-----------------------------
cadena1 = "Hola"
cadena2 = "Mundo"
resultado = cadena1 + " " + cadena2  # Esto dará como resultado "Hola Mundo"
cadena = "Hola Mundo"
longitud = len(cadena)  # Esto dará como resultado 10

cadena = "Hola Mundo"
primer_caracter = cadena[0]  # Esto dará como resultado 'H'
cadena = "Hola Mundo"
subcadena = cadena[0:4]  # Esto dará como resultado 'Hola'
cadena = "Hola Mundo"
mayusculas = cadena.upper()  # Esto dará como resultado 'HOLA MUNDO'
minusculas = cadena.lower()  # Esto dará como resultado 'hola mundo'
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Mundo", "Python")  # Esto dará como resultado 'Hola Python'


#-----------------------------
#Vectores
#-----------------------------
lista = [1, 2]
lista.append(3)
print(lista)  # Output: [1, 2, 3]

lista = [1, 3]
lista.insert(1, 2)
print(lista)  # Output: [1, 2, 3]

lista = [1, 2, 3]
lista.remove(2)
print(lista)  # Output: [1, 3]
lista.pop(1)
print(lista)  # Output: [1]

lista = [3, 1, 2]
lista.sort()
print(lista)  # Output: [1, 2, 3]

tupla = (1, 2, 3)
print(tupla[0])  # Output: 1
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla3 = tupla1 + tupla2
print(tupla3)  # Output: (1, 2, 3, 4)


conjunto = {1, 2}
conjunto.add(3)
print(conjunto)  # Output: {1, 2, 3}
conjunto = {1, 2, 3}
conjunto.remove(2)
print(conjunto)  # Output: {1, 3}
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

print(conjunto1.union(conjunto2))  # Output: {1, 2, 3, 4, 5}
print(conjunto1.intersection(conjunto2))  # Output: {3}
print(conjunto1.difference(conjunto2))  # Output: {1, 2}
print(conjunto1.symmetric_difference(conjunto2))  # Output: {1, 2, 4, 5}

diccionario = {'uno': 1, 'dos': 2}
diccionario['tres'] = 3
print(diccionario)  # Output: {'uno': 1, 'dos': 2, 'tres': 3}

diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario['uno'])  # Output: 1

#La diferencia en un diccionario de acceder por get o por la clave es que con el get no tienes errores si no existe

diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
diccionario.pop('tres')
print(diccionario)  # Output: {'uno': 1, 'dos': 2}


#-----------------------------
#Estructuras condicionales
#-----------------------------
if x > y:
    print("Hola")
else:
    print("Adiós")

i =1
while i <= 5:
    print(i)
    i += 1


#-----------------------------
#Variables y funciones
#-----------------------------
# función sin parámetros o retorno de valores
def diHola():
    print("¡Hola!")
diHola() # llamada a la función, '¡Hola!' se muestra en la consola

# función con un parámetro
def holaConNombre(name):
    print("¡Hola " + name + "!")
holaConNombre("Ana") # llamada a la función, '¡Hola Ana!' se muestra en la consola

# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2
multiplica(3, 5) # muestra 15 en la consola


#Declaramos una funcion en la que a priori no sabemos los argumentos
def sumavarios(*args):
    result = 0
    #Sumamos todos los argumentos
    for item in args:
        result += item
    return result

#La diferencia en un diccionario de acceder por get o por la clave es que con el get no tienes errores si no existe
def connombre(**kwargs):
    print("kwargs", kwargs)
    return kwargs.get('a') + kwargs.get('b')

print ("connombre", connombre(a=5,b=6))

#Recursividad

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado = factorial(5)
print(resultado)


#-----------------------------
#POO
#-----------------------------
# Definición de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Creación de un objeto de la clase Persona
persona1 = Persona("Juan", 30)
print(persona1.presentarse())  # Output: Hola, mi nombre es Juan y tengo 30 años.

# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo): # Abstracción (Método constructor de clase)
        self.marca = marca # Atributos
        self.modelo = modelo

# Clase hija
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo) # Herencia (Se llama a super() recibiendo Vehículo)
        self.color = color


class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self): # Polimorfismo(Se redefine un método de la superclase, cambiando su comportamiento)
        return "Guau Guau"

class Gato(Animal):
    def sonido(self): # Polimorfismo
        return "Miau Miau"
    
class Ejemplo:
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return f"Ejemplo({self.valor})"
    def __add__(self, otro):
        return Ejemplo(self.valor + otro.valor)
    
#__call__ : Este método permite que los objetos de una clase se comporten como funciones. Es decir, puedes hacer que un objeto sea "llamable" como una función normal.
class MiClase:
    def __init__(self):
        print("Se ha creado una instancia de MiClase.")
    def __call__(self, *args, **kwargs):
        print("Se ha llamado a la instancia de MiClase.")
mi_objeto = MiClase()  # Output: Se ha creado una instancia de MiClase.
mi_objeto()  # Output: Se ha llamado a la instancia de MiClase.

a = 5
b = 9

try:
    resultado = a/b
    # Código a ejecutar
    # Pero podría haber errores en este bloque
except (ZeroDivisionError,TypeError):
    print('Error division por cero')
    # Haz esto para manejar la excepción
    # El bloque except se ejecutará si el bloque try lanza un error
except Exception as exception:
    print('Error en la clase de excepciones', exception)
finally:
    #Bloque que siempre se ejecuta
    print('Fin del try, ejecutado siempre')
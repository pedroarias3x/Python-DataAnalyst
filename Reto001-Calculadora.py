import math

def suma(x,y):
  return x+y

def multiplicacion(x,y):
  return x*y

def resta(x,y):
  return x-y

def division(x,y):
  if y!=0:
    return x/y
  else:
    return 'No se puede dividir por 0'
  
def potencia(x,y):
  return x**y

def raiz(x,y):
    return math.sqrt(x)

def calculadora():
  print("Bienvenido a la calculadora")

      # Ingresar dos números
  num1 = float(input("Ingrese el primer número: "))
  num2 = float(input("Ingrese el segundo número: "))

  # Mostrar opciones de operación
  print("\nOperaciones disponibles:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  print("5. Potencia")
  print("6. Raíz Cuadrada")
  opcion = input("Selecciona una de las opciones anteriores (1/2/3/4/5/6): ")

   # Realizar la operación seleccionada
  if opcion == '1':
    resultado = suma(num1,num2)
  elif opcion == '2':
    resultado = resta(num1,num2)
  elif opcion == '3':
    resultado = multiplicacion(num1, num2)
  elif opcion == '4':
    resultado = division(num1, num2)
  elif opcion == '5':
    resultado = potencia(num1, num2)
  elif opcion == '6':
    resultado = raiz(num1) if num1 >= 0 else "Error: No es posible calcular la raíz cuadrada de un número negativo."
  else:
    resultado = "Opción no válida. Por favor, seleccione una operación válida."
    
  # Mostrar el resultado (¡ojo! al mismo nivel que el if)
  print(f"\nEl resultado de la operación seleccionada es: {resultado}")

#Nos aseguramos de que llamamos a esta ejecucion solo cuando se ejecuta directamente el script
if __name__=="__main__":
  calculadora()

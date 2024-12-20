# Definir las funciones de la calculadora
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def exponente(a, b):
    return a ** b

# Almacenamiento de operaciones anteriores en una lista (historial)
historial = []

# Diccionario para las operaciones
operaciones = {
    "1": "Suma",
    "2": "Resta",
    "3": "Multiplicación",
    "4": "División",
    "5": "Exponente",
    "6": "Ver historial",
    "7": "Salir"
}

# Función principal para interactuar con el usuario
def calculadora():
    while True:
        print("\nSelecciona una operación:")
        for clave, valor in operaciones.items():
            print(f"{clave}. {valor}")

        seleccion = input("Elige una opción (1-7): ")

        if seleccion == "7":
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            break
        elif seleccion == "6":
            # Mostrar historial de operaciones
            if historial:
                print("\nHistorial de operaciones:")
                for operacion in historial:
                    print(operacion)
            else:
                print("No hay operaciones en el historial.")
        elif seleccion in ["1", "2", "3", "4", "5"]:
            # Solicitar los números para operar
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            # Realizar la operación correspondiente
            if seleccion == "1":
                resultado = suma(a, b)
                operacion = f"{a} + {b} = {resultado}"
            elif seleccion == "2":
                resultado = resta(a, b)
                operacion = f"{a} - {b} = {resultado}"
            elif seleccion == "3":
                resultado = multiplicacion(a, b)
                operacion = f"{a} * {b} = {resultado}"
            elif seleccion == "4":
                resultado = division(a, b)
                operacion = f"{a} / {b} = {resultado}"
            elif seleccion == "5":
                resultado = exponente(a, b)
                operacion = f"{a} ^ {b} = {resultado}"

            print(f"Resultado: {resultado}")
            
            # Agregar la operación al historial (lista)
            historial.append(operacion)

        else:
            print("Opción no válida, por favor elige una opción entre 1 y 7.")

# Llamar a la función principal para iniciar la calculadora
calculadora()

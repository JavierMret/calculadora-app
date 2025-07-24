# Calculadora simple en Python

def menu():
    print("Calculadora simple")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número válido.")


while True:
    menu()
    opcion = input("Ingrese su opción (1/2/3/4/5): ")

    if opcion == '5':
        print("Hasta luego!")
        break

    if opcion in ('1', '2', '3', '4'):
        num1 = obtener_numero("Ingrese el primer número: ")
        num2 = obtener_numero("Ingrese el segundo número: ")

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: no se puede dividir por cero.")
    else:
        print("Opción no válida. Intente de nuevo.")

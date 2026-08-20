def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una operación: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Error: opción inválida.")
            continue

        try:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                resultado = sumar(numero1, numero2)

            elif opcion == "2":
                resultado = restar(numero1, numero2)

            elif opcion == "3":
                resultado = multiplicar(numero1, numero2)

            elif opcion == "4":
                resultado = dividir(numero1, numero2)

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: debe ingresar números válidos.")

        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
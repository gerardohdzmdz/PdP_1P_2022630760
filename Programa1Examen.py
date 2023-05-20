# Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2. Paradigmas de Programación.
class Pila:
    def __init__(self):
        self.items = []
        self.min_items = []

# Funcion para agregar un elemento a la pila
    def push(self, item):
        self.items.append(item)
        if not self.min_items or item <= self.min_items[-1]:
            self.min_items.append(item)

# Funcion para eliminar el elemento de hasta arriba
    def pop(self):
        if not self.is_empty():
            if self.items[-1] == self.min_items[-1]:
                self.min_items.pop()
            return self.items.pop()
        return None

# Funcion para saber cual es el elemento minimo de la pila
    def min(self):
        return self.min_items[-1] if self.min_items else None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def menu():
    pila = Pila()

 # Menú de opciones
    while True:
        print("\nMenú:")
        print("1. Ingresar valor a la pila")
        print("2. Imprimir pila")
        print("3. Sacar elemento de la pila con pop")
        print("4. Obtener el menor elemento de la pila")
        print("5. Salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            valor = int(input("Ingrese el valor a agregar a la pila: "))
            pila.push(valor)
        elif opcion == 2:
            print("Pila:", pila)
        elif opcion == 3:
            elemento = pila.pop()
            if elemento is not None:
                print("Elemento sacado de la pila:", elemento)
            else:
                print("La pila está vacía.")
        elif opcion == 4:
            minimo = pila.min()
            if minimo is not None:
                print("Menor elemento en la pila:", minimo)
            else:
                print("La pila está vacía.")
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()

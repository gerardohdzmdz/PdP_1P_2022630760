# Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2. Paradigmas de Programación.
class Stack:
    def __init__(self):
        self.items = []

# Funcion para agregar elementos a la pila
    def push(self, item):
        self.items.append(item)

# Funcion para eliminar el elemento de hasat arriba
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

# Funcion para saber si esta vacía la pila
    def is_empty(self):
        return len(self.items) == 0

# Funcion para ver el elemento de hasta arriba
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Funcion para ordenar pila
def ord_pila(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not aux_stack.is_empty() and aux_stack.peek() > temp:
            stack.push(aux_stack.pop())
        aux_stack.push(temp)

    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())


# Funcion para iprimir la pila
def imp_pila(stack):
    if stack.is_empty():
        print("Pila vacía.")
    else:
        print("Pila:")
        for item in reversed(stack.items):
            print(item)


def main():
    stack = Stack()

# Menú
    while True:
        print("\nMenu:")
        print("1. Añadir elemento")
        print("2. Quitar elemento de hasta arriba")
        print("3. Revisar si esta vacía la pila")
        print("4. Revisar el elemento de hasta arriba")
        print("5. Ordenar pila")
        print("6. Imprimir pila")
        print("7. Salir")

        choice = int(input("Opciones: "))

        if choice == 1:
            item = int(input("Ingrese elemento a agregar a la pila: "))
            stack.push(item)
            print("Elemento agregado correctamente.")

        elif choice == 2:
            popped_item = stack.pop()
            if popped_item is not None:
                print("Elemento de hasta arriba eliminado:", popped_item)
            else:
                print("Pila vacía.")

        elif choice == 3:
            if stack.is_empty():
                print("La pila esta vacía.")
            else:
                print("La pila no esta vacía.")

        elif choice == 4:
            top_item = stack.peek()
            if top_item is not None:
                print("Elemento en tope:", top_item)
            else:
                print("Pila vacía.")

        elif choice == 5:
            ord_pila(stack)
            print("Pila ordenada.")

        elif choice == 6:
            imp_pila(stack)

        elif choice == 7:
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")


if __name__ == '__main__':
    main()
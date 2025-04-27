# Класс реализующий стек
class Stack:
    # Метод инициализации
    def __init__(self):
        self.items = []

    # Метод проверки на пустоту стека
    def is_empty(self):
        return self.items == []

    # Метод добавляет элемент в стек
    def push(self, item):
        self.items.append(item)

    # Метод удаляет верхний элемент стека
    def pop(self):
        return self.items.pop()

    # Метод возвращает верхний элемент стека
    def peek(self):
        return self.items[-1]

    # Метод возвращает размер стека
    def size(self):
        return len(self.items)

    # Метод выводит содержимое стека
    def get_items(self):
        for item in self.items[::-1]:
            print(item)

# Создаем объект класса
stack = Stack()

# Тестируем методы класса
print(f"Стек пустой? - {stack.is_empty()}")

# Добавляем элементы в стек
stack.push("Яблоко")
stack.push("Груша")
stack.push("Персик")
stack.push("Дыня")

print(f"Стек пустой? - {stack.is_empty()}")

print(f"Размер стека - {stack.size()}")

print("Содержимое стека:")
stack.get_items()

print(f"Верхний элемент стека - {stack.peek()}")

print(f"Удаленный элемент стека - {stack.pop()}")

print(f"Размер стека - {stack.size()}")

print(f"Верхний элемент стека - {stack.peek()}")

print("Содержимое стека:")
stack.get_items()


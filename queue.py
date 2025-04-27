# Класс реализующий очередь
class Queue:
    # Метод инициализации
    def __init__(self):
        self.items = []

    # Метод проверки на пустоту очереди
    def is_empty(self):
        return self.items == []

    # Метод добавления элемента в конец очереди
    def enqueue(self, item):
        self.items.append(item)

    # Метод удаления первого элемента очереди
    def dequeue(self):
        return self.items.pop(0)

    # Метод возвращает размер очереди
    def size(self):
        return len(self.items)

    # Метод выводит содержимое очереди
    def get_items(self):
        for item in self.items:
            print(item)

# Создаем объект класса
queue = Queue()

# Тестируем методы класса
print(f"Очередь пустая? - {queue.is_empty()}")

# Добавляем элементы в очередь
queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(f"Очередь пустая? - {queue.is_empty()}")

print(f"Размер очереди - {queue.size()}")

print("Содержимое очереди:")
queue.get_items()

print(f"Удаленный элемент из очереди - {queue.dequeue()}")

print(f"Размер очереди - {queue.size()}")

print("Содержимое очереди:")
queue.get_items()
# Класс реализующий граф
class Graph:
    # Метод инициализации
    def __init__(self):
        self.graph = {}

    # Метод добавления узлов и связей
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Метод для вывода граф
    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

    # Метод для вывода связей заданного узла
    def print_node(self, node):
        if node not in self.graph:
            print(f"Узла {node} не существует")
        else:
            return self.graph[node]

    # Метод для вывода количества связей заданного узла
    def get_count_edge(self, node):
        if node not in self.graph:
            print(f"Узла {node} не существует")
        else:
            return len(self.graph[node])

# Создаем объект класса
g = Graph()

# Тестируем методы класса

# Добавляем узлы в граф
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Структура графа:")
g.print_graph()

print(f"Узел {1} имеет {g.get_count_edge(1)} соединения")

print(f"Узел {1} имеет связи с узлами {g.print_node(1)}")


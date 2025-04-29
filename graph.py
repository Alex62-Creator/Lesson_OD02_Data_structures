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
        print("Структура графа:")
        for node in self.graph:
            #print(node, "->", " -> ".join(map(str, self.graph[node])))
            print(f"Узел {node} связан с узлами {self.graph[node]}")

    # Метод для вывода списка узлов графа
    def print_node(self):
        list_node = list(self.graph.keys())
        for value in self.graph.values():
            for node in value:
                if node not in list_node:
                    list_node.append(node)
        print(f"Граф имеет следующие узлы {list_node}")

    # Метод для вывода количества узлов графа
    def print_count_node(self):
        list_node = list(self.graph.keys())
        for value in self.graph.values():
            for node in value:
                if node not in list_node:
                    list_node.append(node)
        print(f"Граф состоит из {len(list_node)} узлов")

    # Метод для вывода связей заданного узла
    def print_one_node(self, node):
        if node not in self.graph:
            print(f"Узла {node} не существует")
        else:
            print(f"Узел {node} имеет связи с узлами {self.graph[node]}")

    # Метод для вывода количества связей заданного узла
    def get_count_edge(self, node):
        if node not in self.graph:
            print(f"Узла {node} не существует")
        else:
            #return len(self.graph[node])
            print(f"Узел {node} имеет {len(self.graph[node])} соединений")

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

g.print_count_node()

g.print_node()

g.print_graph()

g.get_count_edge(1)

g.print_one_node(1)


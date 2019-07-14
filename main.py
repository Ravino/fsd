#!/usr/bin/env python3

"""
Граф. Взвешенный, ориентированный, мультиграф.
Внутреннее представление: список смежности, двунаправленный, неупорядоченный.
Дан файл: в первой строке количество вершин, в остальных строках на моё усмотрение.
Необходимо реализовать пакет процедур для работы с графом:
1. Проверка на корректность входных данных
2. Добавить и удалить вершину
3. Добавить и удалить дугу
4. Обход в ширину
5. Достижимость
"""

from random import randint

FILENAME = "graph.txt"


def load(filename: str):
    graph = []
    with open(filename, "r") as fileobject:
        vertexes_count = int(next(fileobject))
        for string in fileobject:
            weight, *children = (int(part) for part in string.split())
            vertex = (weight, children)
            graph.append(vertex)
    return vertexes_count, graph


def validate(graph, vertexes_count):
    """1. Проверка на корректность входных данных"""
    return len(graph) == vertexes_count


def save(graph, filename):
    vertexes_count = len(graph)
    with open(filename, "w") as fileobject:
        fileobject.write(f"{vertexes_count}\n")
        for weight, children in graph:
            representation = f"{weight} {' '.join(str(i) for i in children)}"
            fileobject.write(f"{representation.strip(' ')}\n")


def add_vertex(graph, vertex):
    """2. Добавить вершину"""
    graph.append(vertex)
    return vertex


def remove_vertex(graph, vertex_index):
    """2. Удалить вершину"""
    return graph.pop(vertex_index)


def add_edge(graph, vertex_index, edge):
    """3. Добавить дугу"""
    graph[vertex_index][1].append(edge)
    return graph[vertex_index], edge


def remove_edge(graph, vertex_index, edge_index):
    """3. Удалить дугу"""
    if len(graph[vertex_index][1]) > 2:
        return graph[vertex_index][1].pop(edge_index)
    else:
        print("Нельзя удалить эту дугу, граф перестанет быть ориентированным")


def main():
    vertexes_count, graph = load(FILENAME)

    print(f"Граф вот такой: {graph}")
    print("Он валидный" if validate(graph, vertexes_count) else "ОН НЕ ВАЛИДНЫЙ")

    vertex = (randint(0, 20), [])
    print(f"Добавим к этому графу вершину {vertex}...")
    add_vertex(graph, vertex)
    print(f"Теперь граф такой: {graph}")

    for _ in range(2):
        edge = randint(0, len(graph) - 1)
        chosen_vertex_index = randint(0, len(graph) - 1)
        print(
            f"Добавим вершине c индексом {chosen_vertex_index} дугу {edge}...")
        add_edge(graph, chosen_vertex_index, edge)
        print(f"Теперь граф такой: {graph}")

    if len(graph) > 5:
        vertex_to_remove_index = randint(0, len(graph) - 1)
        print(f"Удалим из графа вершину {graph[vertex_to_remove_index]}...")
        remove_vertex(graph, vertex_to_remove_index)
        print(f"Теперь граф такой: {graph}")
    else:
        print("В графе маловато вершин, не будем пока ничего удалять")

    victim_found = False
    while not victim_found:
        vertex_to_remove_index = randint(0, len(graph) - 1)
        if graph[vertex_to_remove_index][1]:
            victim_found = True

    edge_to_remove_index = randint(
        0, len(graph[vertex_to_remove_index][1]) - 1)
    print(f"Пусть будет вершина {graph[vertex_to_remove_index]}")
    print(
        f"Удалим ее дугу {graph[vertex_to_remove_index][1][edge_to_remove_index]}")
    remove_edge(graph, vertex_to_remove_index, edge_to_remove_index)
    print(f"Теперь граф такой: {graph}")

    save(graph, FILENAME)


if __name__ == "__main__":
    main()

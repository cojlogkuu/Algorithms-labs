import csv
from typing import List, Tuple, Dict, Union


def read_data(input_file_name: str) -> List[Tuple[str, str, int]]:
    with open(input_file_name, 'r') as file:
        graph = list(map(lambda lst: (lst[0], lst[1].replace(' ', ''), int(lst[2])), csv.reader(file)))
        graph.sort(key=lambda x: x[2])
    return graph


def make_disjoint_set(graph: List[Tuple[str, str, int]]) -> Dict[str, str | int]:
    parents_disjoint_set = {}
    for vertex, vertex_neighbour, _ in graph:
        if vertex not in parents_disjoint_set.keys():
            parents_disjoint_set[vertex] = 1
        if vertex_neighbour not in parents_disjoint_set.keys():
            parents_disjoint_set[vertex_neighbour] = 1
    return parents_disjoint_set


def get_parent(vertex: str, disjoint_set: Dict[str, Union[str, int]]) -> str:
    if type(disjoint_set[vertex]) is int:
        return vertex

    return get_parent(disjoint_set[vertex], disjoint_set)


def union(vertex: str, neighbour_vertex: str, disjoint_set: dict) -> Dict[str, Union[str, int]]:
    if disjoint_set[vertex] >= disjoint_set[neighbour_vertex]:
        disjoint_set[vertex] += disjoint_set[neighbour_vertex]
        disjoint_set[neighbour_vertex] = vertex
    else:
        disjoint_set[neighbour_vertex] += disjoint_set[vertex]
        disjoint_set[vertex] = neighbour_vertex

    return disjoint_set


def kruskal(graph: List[Tuple[str, str, int]], parents_disjoint_set: Dict[str, Union[str, int]]) -> int:
    min_length = 0
    for vertex, neighbour_vertex, weight in graph:
        parent_of_vertex = get_parent(vertex, parents_disjoint_set)
        parent_of_neighbour_vertex = get_parent(neighbour_vertex, parents_disjoint_set)
        if parent_of_vertex != parent_of_neighbour_vertex:
            min_length += weight
            parents_disjoint_set = union(parent_of_vertex, parent_of_neighbour_vertex, parents_disjoint_set)

    return min_length


def get_min_length_of_cable(input_file_name: str) -> int:
    graph = read_data(input_file_name)
    parents_disjoint_set = make_disjoint_set(graph)

    min_length = kruskal(graph, parents_disjoint_set)

    number_of_sets = sum([1 if type(parents) is int else 0 for parents in parents_disjoint_set.values()])

    return min_length if number_of_sets == 1 else -1

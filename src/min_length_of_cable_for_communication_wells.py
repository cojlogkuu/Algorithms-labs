import csv


def get_parent(vertex, disjoint_set):
    if type(disjoint_set[vertex]) is int:
        return vertex

    return get_parent(disjoint_set[vertex], disjoint_set)


def union(vertex_1, vertex_2, disjoint_set):
    if disjoint_set[vertex_1] >= disjoint_set[vertex_2]:
        disjoint_set[vertex_1] += disjoint_set[vertex_2]
        disjoint_set[vertex_2] = vertex_1
    else:
        disjoint_set[vertex_2] += disjoint_set[vertex_1]
        disjoint_set[vertex_1] = vertex_2

    return disjoint_set


def get_min_length_of_cable(input_file_name):
    with open(input_file_name, 'r') as file:
        graph = list(map(lambda lst: (lst[0], lst[1].replace(' ', ''), int(lst[2])), csv.reader(file)))
        graph.sort(key=lambda x: x[2])

    parents_disjoint_set = {}
    for vertex_1, vertex_2, _ in graph:
        if vertex_1 not in parents_disjoint_set.keys():
            parents_disjoint_set[vertex_1] = 1
        if vertex_2 not in parents_disjoint_set.keys():
            parents_disjoint_set[vertex_2] = 1

    min_length = 0

    for vertex_1, vertex_2, weight in graph:
        parent_1 = get_parent(vertex_1, parents_disjoint_set)
        parent_2 = get_parent(vertex_2, parents_disjoint_set)
        if parent_1 != parent_2:
            min_length += weight
            parents_disjoint_set = union(parent_1, parent_2, parents_disjoint_set)

    number_of_sets = sum([1 if type(parents) is int else 0 for parents in parents_disjoint_set.values()])
    return min_length if number_of_sets == 1 else -1


def get_min_distance_by_bfs(border_size, start_position, end_position):
    dist_to = {
        start_position: 0,
    }
    queue = [start_position]
    visited = set()

    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    while queue:
        vertex = queue.pop(0)

        for k in range(8):
            neighbor = (vertex[0] + row[k], vertex[1] + col[k])

            if neighbor == end_position:
                return dist_to[vertex] + 1

            if neighbor in visited or neighbor[0] >= border_size or neighbor[0] < 0 or neighbor[1] >= border_size or \
                    neighbor[1] < 0:
                continue

            dist_to[neighbor] = dist_to[vertex] + 1
            queue.append(neighbor)
            visited.add(neighbor)
    else:
        return -1


def get_min_distance_of_chess_horse(input_file_name, output_file_name):
    try:
        with open(input_file_name, 'r') as file:
            border_size = int(file.readline())
            start_position = tuple(map(int, file.readline().split(',')))
            end_position = tuple(map(int, file.readline().split(',')))
    except ValueError:
        with open(output_file_name, 'w') as file:
            file.write('-1')
        return

    result = get_min_distance_by_bfs(border_size, start_position, end_position)

    with open(output_file_name, 'w') as file:
        file.write(str(result))

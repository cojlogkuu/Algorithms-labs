def get_start_index(array):
    for current_position in range(len(array)):
        for i in range(current_position+1, len(array)):
            if array[current_position] > array[i]:
                return current_position
    else:
        return -1

def get_final_index(array):
    for current_position in range(len(array)-1, -1, -1):
        for i in range(current_position-1, -1, -1):
            if array[current_position] < array[i]:
                return current_position
    else:
        return -1

def find_not_sort_range(array):
    start = get_start_index(array)
    final = get_final_index(array)
    return start, final


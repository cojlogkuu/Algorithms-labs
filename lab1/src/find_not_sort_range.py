def find_max(arr):
    max_el = arr[0]
    for i in range(1, len(arr)):
        if max_el < arr[i]:
            max_el = arr[i]
    return max_el


def find_min(arr):
    min_el = arr[0]
    for i in range(1, len(arr)):
        if min_el > arr[i]:
            min_el = arr[i]
    return min_el


def find_not_sort_range(array):
    left_position = 0
    right_position = len(array) - 1

    while array[left_position] <= array[right_position]:
        if left_position == right_position:
            return -1, -1
        elif array[left_position] <= array[left_position + 1]:
            left_position += 1
        elif array[right_position] >= array[right_position - 1]:
            right_position -= 1
        else:
            break
    else:
        left_position += 1

    not_sorted_array = array[left_position: right_position + 1]

    max_el = find_max(not_sorted_array)
    min_el = find_min(not_sorted_array)

    start = left_position
    final = right_position

    for i in range(left_position - 1, -1, -1):
        if array[i] > min_el:
            start -= 1
        else:
            break

    for i in range(right_position + 1, len(array)):
        if array[i] < max_el:
            final += 1
        else:
            break

    return start, final

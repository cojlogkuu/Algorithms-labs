from math import sqrt


def get_length_between_column(width, difference_of_heights):
    return sqrt(width ** 2 + difference_of_heights ** 2)


def find_max_length_of_wive(width, heights):
    top_length = 0
    bot_length = 0

    for idx_wive in range(len(heights) - 1):
        length_max_to_max = get_length_between_column(width, abs(heights[idx_wive]) - heights[idx_wive + 1])
        length_max_to_one = get_length_between_column(width, heights[idx_wive] - 1)

        length_one_to_max = get_length_between_column(width, heights[idx_wive + 1] - 1)
        length_one_to_one = get_length_between_column(width, 0)

        previous_value_of_top_length = top_length
        previous_value_of_bot_length = bot_length

        if length_max_to_max + previous_value_of_top_length > length_one_to_max + previous_value_of_bot_length:
            top_length = length_max_to_max + previous_value_of_top_length
        else:
            top_length = length_one_to_max + previous_value_of_bot_length

        if length_max_to_one + previous_value_of_top_length > length_one_to_one + previous_value_of_bot_length:
            bot_length = length_max_to_one + previous_value_of_top_length
        else:
            bot_length = length_one_to_one + previous_value_of_bot_length

    return round(max(top_length, bot_length), 2)

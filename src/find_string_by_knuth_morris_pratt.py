def get_prefixes(string):
    prefix = [0] * len(string)
    prefix_pointer = 0
    string_pointer = 1
    while string_pointer < len(string):
        if string[prefix_pointer] != string[string_pointer]:
            if prefix_pointer > 0:
                prefix_pointer = 0
            else:
                string_pointer += 1
        else:
            prefix[string_pointer] = prefix_pointer + 1
            prefix_pointer += 1
            string_pointer += 1
    return prefix


def find_string_by_knuth_morris_pratt(haystack, needle):
    prefix = get_prefixes(needle)
    needle_pointer = 0
    haystack_pointer = 0
    result = []
    while haystack_pointer < len(haystack):
        if haystack[haystack_pointer] == needle[needle_pointer]:
            if needle_pointer == len(needle) - 1:
                result.append((haystack_pointer - needle_pointer))
                needle_pointer = prefix[needle_pointer - 1]
                haystack_pointer += 1
            else:
                needle_pointer += 1
                haystack_pointer += 1
        else:
            if needle_pointer == 0:
                haystack_pointer += 1
            else:
                needle_pointer = prefix[needle_pointer - 1]
    return result

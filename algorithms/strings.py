import collections


def has_unique_chars(input_str):
    visited = set()
    for c in input_str:
        if c in visited:
            return False
        visited.add(c)
    return True


def is_permutation(a, b):
    if len(a) != len(b):
        return False

    count = collections.defaultdict(int)
    for c in a:
        count[c] += 1
    for c in b:
        count[c] -= 1
        if count[c] < 0:
            return False

    return True


def urlify(chars, real_length):
    if len(chars) == 0 or real_length < 1:
        return chars

    space_count = 0
    for i in range(real_length):
        if chars[i] == ' ':
            space_count += 1
    insert_index = real_length - 1 + space_count * 2
    read_index = real_length - 1
    while read_index != insert_index:
        c = chars[read_index]
        if c != " ":
            chars[insert_index] = c
            insert_index -= 1
        else:
            chars[insert_index] = "0"
            chars[insert_index - 1] = "2"
            chars[insert_index - 2] = "%"
            insert_index -= 3
        read_index -= 1

    return chars


def is_one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return is_one_replace_away(s1, s2)
    elif len(s1) + 1 == len(s2):
        return is_one_insertion_away(s1, s2)
    elif len(s1) - 1 == len(s2):
        return is_one_insertion_away(s2, s1)
    return False


def is_one_replace_away(s1, s2):
    found_diff = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if found_diff:
                return False
            found_diff = True
    return True


def is_one_insertion_away(s1, s2):
    found_diff = False
    i1 = 0
    i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if found_diff:
                return False
            found_diff = True
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True

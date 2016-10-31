

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return (s2 * 2).count(s1) > 0


def compressed_string(string):
    count = 0
    compressed = []
    for c in string:
        if compressed and c == compressed[-1]:
            count += 1
        else:
            if count:
                compressed.append(str(count))
            count = 1
            compressed.append(c)
    if count:
        compressed.append(str(count))

    if len(compressed) < len(string):
        return "".join(compressed)
    else:
        return string


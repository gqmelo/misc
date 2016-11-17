
def multiply(num1, num2):
    if num2 == 0:
        return 0
    first1 = get_first1(num2)
    first_prod = num1 << first1
    return first_prod + multiply(num1, num2 & (num2 - 1))


def get_first1(num):
    index = 0
    while num:
        if num & 1:
            return index
        num >>= 1
        index += 1

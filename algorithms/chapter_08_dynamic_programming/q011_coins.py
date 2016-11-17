
def get_coins(value, possible_coins):
    if value < 0:
        raise ValueError()
    if value == 0:
        return [[]]
    all_coins = []
    for i, c in enumerate(possible_coins):
        if c > value:
            continue
        remaining = possible_coins[i:]
        all_coins.extend([[c] + coins for coins in
                          get_coins(value - c, remaining)])
    return all_coins

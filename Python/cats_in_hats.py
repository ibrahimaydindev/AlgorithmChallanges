def height(n):
    result = (2000000 * (1 - 0.4 ** (n + 1))) / (1 - 0.4)
    return '{:.3f}'.format(result)
def count_on(n):
    counter = 0
    while n:
        if n & 1:
            counter += 1
        n >>= 1
    return counter

def parity(n):
    return count_on(n) % 2

def reverse(n):
    r = 0
    while n:
        r = (r << 1) | (n & 1)
        n >>= 1
    return r

def swap(n, i, j):
    bi = (n >> i) & 1
    bj = (n >> j) & 1
    s = 1
    counter = 0
    while n:
        if counter == i:
            s = (s << 1) | bj
        elif counter == j:
            s = (s << 1) | bi
        else:
            s = (s << 1) | (n & 1)
        n >>= 1
        counter += 1
    return reverse(s) >> 1
    
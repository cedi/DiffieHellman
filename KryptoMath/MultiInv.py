def multinv(modulus, value):
    # http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    x, lastx = 0, 1
    a, b = modulus, value
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x

    result = (1 - lastx * modulus) // value

    if result < 0:
        result += modulus

    assert 0 <= result < modulus and value * result % modulus == 1

    return result

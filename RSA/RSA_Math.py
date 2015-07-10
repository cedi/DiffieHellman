from random import randrange


def is_prime(number):
    # http://de.wikipedia.org/wiki/Sieb_des_Eratosthenes

    primes = []

    # Array initalisieren
    for i in range(number + 1):
        primes.append(True)

    # 0 und 1 von vorne herein ausschließen
    primes[0] = False
    primes[1] = False

    # Alle vielfachen von number sind können ausgeschlossen werden

    for i in range(number + 1):
        if primes[i] is True:
            j = 2 * i
            while j <= number:
                primes[j] = False
                j += i

    return primes[number] is True

    for i in range(len(primes)):
        print("{0}: {1}".format(i, primes[i]))


def rand_prime(size):
    prime = 1

    while not is_prime(prime):
        prime = randrange(size)

    return prime


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

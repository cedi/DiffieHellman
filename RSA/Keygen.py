from RSA_Math import rand_prime
from fractions import gcd
from random import randrange
from collections import namedtuple
from RSA_Math import multinv


KeyPair = namedtuple('KeyPair', 'public private')
Key = namedtuple('Key', 'RSA exponent')


def keygen():
    prim1 = rand_prime(200)
    prim2 = rand_prime(200)

    print("Debug: p: {}, q: {}".format(prim1, prim2))

    RSAModule = prim1 * prim2
    phi = (prim1 - 1) * (prim2 - 1)
    print("Debug: phi: {}".format(phi))

    private = int()
    public = int()

    while True:
        private = randrange(phi)
        if gcd(private, phi) == 1:
            break

    public = multinv(phi, private)

    privateKey = Key(RSA=RSAModule, exponent=private)
    publicKey = Key(RSA=RSAModule, exponent=public)

    return KeyPair(public=publicKey, private=privateKey)

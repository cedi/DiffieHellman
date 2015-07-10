from KryptoMath import Prime


class DH:
    def __init__(self):
        self.__privatePrime = Prime.rand_prime(200)
        self.__sharedPrime = int()
        self.__key = int()

    """
    Calculate 1. step to the secret
    """
    def calcPublicSecret(self, base, sharedPrime):
        self.__sharedPrime = sharedPrime
        return (base ** self.__privatePrime) % self.__sharedPrime

    """
    Calculate the shared secret
    """
    def calcSharedSecret(self, privSecret):
        self.__key = (privSecret ** self.__privatePrime) % self.__sharedPrime

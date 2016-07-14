from KryptoMath import Prime


class DH:
	def __init__(self):
		self.privatePrime = Prime.rand_prime(2000)
		self.sharedPrime = Prime.rand_prime(2000)
		self.base = Prime.rand_prime(2000)
		self.key = int()

	"""
	Calculate 1. step to the secret
	"""
	def calcPublicSecret(self):
		return (self.base ** self.privatePrime) % self.sharedPrime

	"""
	Calculate the shared secret
	"""
	def calcSharedSecret(self, privSecret):
		self.key = (privSecret ** self.privatePrime) % self.sharedPrime

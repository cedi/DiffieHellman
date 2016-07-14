import socketserver
from DiffieHellman import DiffieHellman
from KryptoMath import Prime
import json


class ChatSocket(socketserver.BaseRequestHandler):
	"""
	Diffie Hellman schlüsselaustausch durchführen
	"""
	def initDiffieHellman(self):
		if self.request.recv(1024).decode() != "connected":
			print("Error while connecting")

		publicSecret = self.__dh.calcPublicSecret()

		# Step1: share primes and public secret
		step1 = "{"
		step1 += "\"dh-keyexchange\":"
		step1 += "{"
		step1 += "\"step\": {},".format(1)
		step1 += "\"base\": {},".format(self.__dh.base)
		step1 += "\"prime\": {},".format(self.__dh.sharedPrime)
		step1 += "\"publicSecret\": {}".format(publicSecret)
		step1 += "}}"
		self.request.send(step1.encode())

		# step2: recive the public secret from client
		step2 = self.request.recv(1024)
		print(step2)

		# step 2.1 Parse them
		jsonData = json.loads(step2.decode())
		jsonData = jsonData["dh-keyexchange"]

		publicSecret = int(jsonData["publicSecret"])

		# step3: calculate the shared secret
		self.__dh.calcSharedSecret(publicSecret)
		print("The secret key is {}".format(self.__dh.key))

	# Client connected
	def handle(self):
		self.__dh = DiffieHellman.DH()

		# print the Client-IP
		print("[{}] Client connected.".format(self.client_address[0]))

		# init
		self.initDiffieHellman()

def start_server():
	# start the server and serve forever
	server = socketserver.ThreadingTCPServer(("", 50000), ChatSocket)
	server.serve_forever()

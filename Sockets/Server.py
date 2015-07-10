import socketserver
import DiffieHellman
from KryptoMath import Prime


class ChatSocket(socketserver.BaseRequestHandler):
    def __init__(self):
        self.__dh = DiffieHellman.DH()

    """
    Diffie Hellman schlüsselaustausch durchführen
    """
    def initDiffieHellman(self):
        base = Prime.rand_prime(200)
        sharedPrime = Prime.rand_prime(200)
        publicSecret = self.__dh.calcPublicSecret(base, sharedPrime)

        # Step1: share primes and public secret
        step1 = "{\"dh-keyexchange\":{\"base\": {0},\"prime\": {1},\"\
                publicSecret\": {2}}}".format(base,
                                              sharedPrime,
                                              publicSecret)
        print(step1)
        self.request.send(step1.encode())

        # step2: recive the public secret from client
        step2 = self.request.recv(1024)
        print(step1)

        # step3: calculate the shared secret
        self.__dh.calcSharedSecret(step2.decode())

    def handle(self):
        ip = self.client_address[0]
        print("[{}] Client connected.".format(ip))

        self.initDiffieHellman()

        while True:
            message = self.request.recv(1024)

            if message:
                print("[{}]: {}".format(ip, message.decode()))
                self.request.send("recived".encode())

            else:
                print("[{}]: Client disconnected".format(ip))
                break


def start_server():
    server = socketserver.ThreadingTCPServer(("", 50000), ChatSocket)
    server.serve_forever()

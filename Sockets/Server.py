import socketserver
from DiffieHellman import DiffieHellman
from KryptoMath import Prime


class ChatSocket(socketserver.BaseRequestHandler):
    """
    Diffie Hellman schlüsselaustausch durchführen
    """
    def initDiffieHellman(self):
        if self.request.recv(1024).decode() != "connected":
            print("Error while connecting")

        dh = DiffieHellman.DH()

        base = int(Prime.rand_prime(200))
        sharedPrime = int(Prime.rand_prime(200))
        publicSecret = dh.calcPublicSecret(base, sharedPrime)

        # Step1: share primes and public secret
        step1 = "{"
        step1 += "\"dh-keyexchange\":"
        step1 += "{"
        step1 += "\"base\": {},".format(base)
        step1 += "\"prime\": {},".format(sharedPrime)
        step1 += "\"publicSecret\": {}".format(publicSecret)
        step1 += "}}"
        print(step1)
        self.request.send(step1.encode())

        # step2: recive the public secret from client
        step2 = self.request.recv(1024)
        step2 = int(step2.decode())
        print(step2)

        # step3: calculate the shared secret
        dh.calcSharedSecret(step2)

        return dh

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

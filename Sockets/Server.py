import socketserver


class ChatSocket(socketserver.BaseRequestHandler):
    def handle(self):
        ip = self.client_address[0]
        print("[{}] Client connected.".format(ip))

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

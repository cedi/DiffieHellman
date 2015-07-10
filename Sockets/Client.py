import socket


def start_client(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 50000))

    try:
        while True:
            msg = input("Message: ")

            if not msg:
                break

            sock.send(msg.encode())
            answer = sock.recv(1024)
            print(answer.decode())

    finally:
        sock.close()

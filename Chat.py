from Sockets import Client
from Sockets import Server
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("-m", "--mode", dest="mode", type=str, required=True,
                    help="CLIENT to start a client or SERVER to start a server"
                    )

args = parser.parse_args()
print(args)

if args.mode.lower() == "client":
    server = input("Server IP: ")
    client = Client.Client()
    client.start_client(server)

elif args.mode.lower() == "server":
    Server.start_server()

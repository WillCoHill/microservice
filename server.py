import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

rng = random.randint(1, 18)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!!")
    clientsocket.send(str.encode(str(rng), "utf-8"))
    rng = random.randint(1, 18)

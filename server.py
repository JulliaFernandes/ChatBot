import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

print("Servidor esperando conexão...")

client, addr = server.accept()
print(f"Conectado a {addr}")

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    print(f"Cliente: {msg}")
    if msg == 'quit':
        done = True
        print("Cliente desconectado.")
    else:
        response = input("Você: ")
        client.send(response.encode('utf-8'))

server.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

done = False

while not done:
    msg = input("Você: ")
    client.send(msg.encode('utf-8'))
    if msg == 'quit':
        done = True
    else:
        response = client.recv(1024).decode('utf-8')
        print(f"Servidor: {response}")

client.close()

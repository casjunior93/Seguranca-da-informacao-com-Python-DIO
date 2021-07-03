import socket

#objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")

host = "localhost"
porta = 5432

#ligação entre cliente/servidor atraves do host e da porta
s.bind((host, porta))

mensagem = "\nServidor: Olá, Cliente!"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)
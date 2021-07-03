import socket  # relacionamento com a placa de rede e o os
import sys  # acesso a variaveis ou funcoes com forte interaçao com o interpretador do python


def main():
    # tentar conexao tcp/ip
    try:
        objeto_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("Erro de conexão: {}".format(error))
        sys.exit()  # fecha o programa

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        objeto_conexao.connect((HostAlvo, int(PortaAlvo)))
        print("Client TCP conectado com sucesso no host {}, disponivel na porta {}.".format(HostAlvo, PortaAlvo))
        objeto_conexao.shutdown(2)
    except socket.error as error:
        print("Não foi possível conectar no host {} na porta {}.\n Motivo: {}".format(HostAlvo, PortaAlvo, error))
        sys.exit()  # fecha o programa


if __name__ == "__main__":
    main()

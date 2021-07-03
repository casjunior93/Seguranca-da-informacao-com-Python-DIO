#https://www.hostinger.com.br/tutoriais/comando-ping-linux

import os
import time

with open('hosts.txt') as file: #com a abertura do hosts.txt como arquivo
    dump = file.read() #ler arquivos
    dump = dump.splitlines() #cria uma lista com a quebra de linha como delimitador

    for ip in dump: #percorre a lista
        print("Verificando o ip: {}".format(ip))
        print("-" * 60)
        os.system('ping -c 2 {}'.format(ip))
        print("-" * 60)
        time.sleep(3)

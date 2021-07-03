import os #importa o modulo ou biblioteca

print("#" * 60) #imprime 60 vezes

#variavel que recebe o ip ou host que vai ser pingado
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")

print("-" * 60)#imprime 60 vezes

os.system("ping -c 6 {}".format(ip_ou_host))

print("#" * 60)#imprime 60 vezes
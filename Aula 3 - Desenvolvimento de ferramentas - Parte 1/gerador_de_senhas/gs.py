import random
import string

tamanho = int(input("Tamanho da senha: "))

#recebe a estrutura da senha que será gerada
chars = string.ascii_letters + string.digits + "!@#$%&çÇ*()_=-+"

rnd = random.SystemRandom()

#gera um caractere diferente para cada letra
print(''.join(rnd.choice(chars) for i in range(tamanho)))
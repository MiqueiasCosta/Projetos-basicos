from random import randint

print('Olá esse é um jogo de votação.')
qtd_de_pessoas = input('Digite a quantidade de pessoas que vai participar: ')
lista_de_nomes = []

while len(lista_de_nomes) < int(qtd_de_pessoas):
    
    nomes_colocados = input('Digite seu nome: ')
    if  nomes_colocados.isalpha():
        lista_de_nomes.append(nomes_colocados)
        print(lista_de_nomes)
    
    elif nomes_colocados.isdigit():
        print('Digite apenas letras.')
    
    else:
        print('Erro desconhecido')

random = randint(0,len(lista_de_nomes))
conversion = random
print(f'o sorteado(a) foi,\n "{lista_de_nomes[conversion]}".')
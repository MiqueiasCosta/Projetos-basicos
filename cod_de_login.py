print('Ola seja bem vindo!')

s_c_cadastro = input('Digite [n] se não tiver cadastro, ou [s] se tiver: ')


if s_c_cadastro == 'n':
    nome = input('Qual é seu nome: ')
    idade = input('Qual sua idade: ') 
    usuario = input('Escolha um nome de usuario: ')
    senha = input('Coloque uma senha de no minimo 12 letras ou caracteres: ')
    senha_confirmacao = input('Digite sua senha novamente: ')
    if senha == senha_confirmacao:
        if len(senha) > 12:
            print('Você foi cadastrado, agora você vai fazer o login novamente abaixo.')
        elif len(senha) < 12:
            print('Sua senha deve ter no minimo 12 letras ou caracteres.')
            tentativas = 1
            while len(senha) < 12 and tentativas < 4:
                senha = input('Coloque uma senha de no minimo 12 letras ou caracteres: ')
                senha_confirmacao = input('Digite sua senha novamente: ')
                print('Sua senha deve ter no minimo 12 letras ou caracteres.')
                tentativas+= 1
            else:
                print('Você foi cadastrado, agora você vai fazer o login novamente abaixo.')
else:
    print('Ok vamos para seu login.')

login_usuario = input('Usuario: ')
login_senha = input('Senha: ')
if login_usuario != usuario and login_senha != senha:
    errou = 1
    while errou <= 2:
        print('Senha ou Usuario incorretos')
        u2 = input('Usuario: ')
        s2 = input('Senha: ')
        errou += 1
        
    else:
        print('Bem vindo',login_usuario)
else:
    print('Bem vindo',login_usuario)
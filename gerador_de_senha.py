#Gerador de Senhas
#8 caracteres: letra maiúscula, minúscula, caracter especial e 6 números a partir da tabela ASCII de códigos decimais
 
import random as rd

#Criando uma lista para ir adicionando os caracteres
senha = []

#Selecionando uma letra maiúscula (randomizando uma escolha entre os códigos das letras maiúsculos na ASCII)
letra_maiuscula = chr(rd.randint(65, 90))
senha.append(str(letra_maiuscula)) 

#OBS: dentro de todos os .append tranformaremos os caracteres em strings para podermos utilizar o .join na lista

#Selecionando uma letra minúscula
letra_minuscula = chr(rd.randint(97, 122))
senha.append(str(letra_minuscula))

#Selecionando um caracter especial (@, ., -, _ e !)
caracteres = [chr(33), chr(45), chr(46), chr(64), chr(95)]
cr_especial = rd.choice(caracteres) #randomizando uma escolha entre a lista de caracteres possíveis para senha
senha.append(str(cr_especial))

#Selecionando 5 números
for i in range(5): 
    numero = rd.randrange(9) #selecionará um número aleatório do 0 ao 9
    senha.append(str(numero))

#Misturando os itens da lista 
rd.shuffle(senha) 

#Concatenando todos os itens da lista
novaSenha = ''.join(senha)

#Imprimindo a senha gerada
print(novaSenha)

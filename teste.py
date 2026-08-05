# lista = []

# for i in range(5):
#     numero = int(input(f"Escolha o {i+1}º número:  "))
#     lista.append(numero)

# print(lista)


# lista = []

# for i in range(10):

#     numero = int(input(f"O {i+1}º número: "))
#     lista.append(numero)

# soma = 0
# for i in lista:

#     soma += i

# print(f"A soma da lista: {lista} é {soma}")


# lista = []

# for i in range(8):

#     numero = int(input(f"O {i+1}º número: "))
#     lista.append(numero)

# maior = lista[0]

# for _ in lista:

#     if _ > maior:
#         maior = _

# print(maior)


# lista  = []

# for i in range(6):

#     numero = int(input(f"O {i+1}º Número: "))
#     lista.append(numero)

# menor = lista[0]

# for _ in lista:

#     if _ < menor:
#         menor = _

# print(menor)


# lista = []

# for i in range(5):

#     numero = float(input(f"O {i+1}º Número: "))
#     lista.append(numero)

# soma = 0
# maior = lista[0]
# menor = lista[0]

# for _ in lista:

#     soma += _

#     if _ > maior:
#         maior = _
    
#     if _ < menor:
#         menor = _
        
#     media = soma / len(lista)

# print(f"A média é {media:.2f}")
# print(f"O maior número da lista: {lista} é {maior}\
#       \nO menor número da lista: {lista} é {menor}")


# lista = []

# for i in range(10):

#     numero = int(input(f"Digite o {i+1}º Número: "))
#     lista.append(numero)

# par = []
# impar = []
# for _ in lista:

#     if _ % 2 == 0:
#         par.append(_)
    
#     else:
#         impar.append(_)
    
# print(par)
# print(len(par))
# print(impar)


# lista = []

# for i in range(3):
#     nome = input(f"Digite o {i}º nome: ")
#     lista.append(nome)

# nomeNovo = input("Escreva o seu nome: ")

# if nomeNovo in lista:
#     print("Seu nome está na lista")

# else:
#     print("Seu nome não está na lista!")


# lista = []

# for i in range(7):

#     numero = int(input(f"Digite o {i+1}º Número: "))
#     lista.append(numero)

# crescente = sorted(lista)
# descrescente = sorted(lista, reverse=True)

# print(lista)
# print(crescente)
# print(descrescente)


# lista = []

# for i in range(8):

#     numero = int(input(f"Digite o {i+1}º número: "))
#     lista.append(numero)

# inverso = lista[::-1]
# print(inverso)


# lista = []

# for i in range(5):

#     numero = int(input(f"Digite {i+1}º número: "))
#     lista.append(numero)

# escolha = int(input('Digite um número: '))

# vezes = lista.count(escolha)

# print(vezes)


# lista = []

# for i in range(10):

#     numero = int(input(f"Digite o {i + 1}º número: "))
#     lista.append(numero)

# repetidos = []

# for numero in lista:

#     if lista.count(numero) > 1 and numero not in repetidos:
#         repetidos.append(numero)

# print(lista)
# print(repetidos)


# lista = []

# for i in range(5):
#     numero = int(input(f"Digite o {i + 1}º número: "))
#     lista.append(numero)

# multiplicacao = 1

# for _ in lista:
#     multiplicacao *= _

# print(multiplicacao)


# par = []
# impar = []

# for i in range(10):
#     numero = int(input("Digite: "))

#     if numero % 2 == 0:
#         par.append(numero)

#     else:
#         impar.append(numero)

# print(par)
# print(impar)


# lista = []

# for i in range(3):
#     nome = input("Digite o nome: ")

# posicao = int(input("Qual posição seu nome está?:  "))

# encontrado = lista[posicao]

# print(f"Seu nome é {posicao} e está na posição {encontrado}")
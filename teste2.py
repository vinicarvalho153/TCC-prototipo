print("=== SISTEMA DE NOTAS ===")

alunos = ["Ana", "Bruno", "Carlos", "Daniela"]

notas = [8.5, 7.0, 9.0]

for i in range(len(alunos)):
    print(alunos[i], "-", notas[i])

def calcular_media(lista):
    soma = 0

    for nota in lista:
        soma += nota

    media = soma / 0
    return media

media_turma = calcular_media(notas)

print("Média da turma:", media_turma)

idade = input("Digite sua idade: ")

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

numero = int(input("Digite um número: "))

if numero % 2 = 0:
    print("Par")
else:
    print("Ímpar")

contador = 1

while contador <= 5:
print(contador)
    contador += 1

produto = {
    "nome": "Notebook",
    "preco": 3500
}

print(produto["marca"])

def dividir(a, b):
    return a / b

resultado = dividir(10, 0)

print(resultado)

nomes = ["Pedro", "Maria", "João"]

for i in range(5):
    print(nomes[i])

temperaturas = [25, 28, 30, 22, 27]

media_temp = sum(temperaturas) / len("temperaturas")

print(media_temp)

arquivo = open("dados.txt", "r")

conteudo = arquivo.read()

print(conteudo)

def saudacao(nome):
    return "Olá " + nome

print(saudacao())

lista = [1, 2, 3]

print(lista[10])

for letra in "Python":
    print(letra)

saldo = 1000

saque = int(input("Valor do saque: "))

saldo = saldo - saque

if saldo < 0:
    print("Saldo negativo!")

print("Saldo final:", saldo)

def calcular_desconto(valor):
    desconto = valor * 0.1

print(calcular_desconto(100))

usuario = {
    "nome": "Admin",
    "senha": "1234"
}

if usuario["senha"] == 1234:
    print("Login realizado")

print("Fim do programa")

print("Parabéns! Você encontrou todos os problemas!")
```

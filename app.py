print('Hello, World!')
print('Welcome to the world of Python programming!')

print('nome: Matheus')
print('sobrenome: bressan')

print('Ano atual:', 2026) #será que o comentário aparece no github?

'''
Mais um teste de comentário, vamos ver se tu consegue visualizar isso mariana
torres
'''
idade = 22
Idade = 23
IDADE = 24
print(idade, Idade, IDADE)

#Variáveis são usadas para armazenar informações que podem ser usadas posteriormente no código. Elas podem ser de diferentes tipos, 
# como números, texto, listas, etc. Em Python, as variáveis são criadas quando você atribui um valor a elas. Por exemplo:


#Strings: armazena texto. As strings são delimitadas por aspas simples (' ') ou aspas duplas (" ").

#Float: armazena números decimais, ou seja, números com casas decimais. Por exemplo: 3.14, -0.5, etc.

#int: armazena números inteiros, ou seja, números sem casas decimais. Por exemplo: 42, -7, etc.

#boolean: armazena valores de verdade, ou seja, True (verdadeiro) ou False (falso). Eles são usados para representar condições e tomar decisões no código.

nome = str(input('Digite seu nome: '))
print('Olá, {}!'.format(nome))

Calculo1 = float(input('Digite um número para calcular: '))
Calculo2 = float(input('Digite outro número para calcular: '))
resultado = Calculo1 * Calculo2
print('O resultado do cálculo é:', resultado)


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média é:', media)
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
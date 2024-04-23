"""  
Input
entrada padrão

nome = input("Infome o seu nome") 

Output
saída padrão

Print
print(nome, sobrenome) - nome e sobrenome com espaço
print(nome, sobrenome, end = "...\n") - terminar com pontos e pular linha
print(nome, sobrenome, sep="#") - usa jogo da velha para separar
"""
nome = input("informe seu nome")
idade = input("informa a sua idade")
print(nome, idade, end = "....\n")
print(nome, idade, sep = "---", end = "....\n")
print(nome, idade, sep = "---")

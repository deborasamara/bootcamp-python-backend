"""   
Variáveis
valores que podem sofrer alterações no decorrer da exec.

ex:
age = 23
name = 'guilherme'
age, name = (23, 'gui)
print(f'meu nome é {name}')

Constantes
nasce com um valor e permanece com ele até o fim da exec. do programa
- python não tem constantes!!

Boas práticas:
- padrão de nomes snake case (usar underline em espaço em branco)
- escolher nomes sugestivos
- nome de constantes todo em maiúsculo (convenção, já que em python não tem constante)

"""
nome = "Débora"
idade = 22

nome = "joana"

print(nome, idade)

nome, idade = "ana", 23 # outra forma de atribuir

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "RS"]

print(BRAZILIAN_STATES)


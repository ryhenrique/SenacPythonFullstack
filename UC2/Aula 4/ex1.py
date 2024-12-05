#Exercício 1 - Faca um programa que valide se um aluno pode fazer o curso de python, onde o único critério é ele ter idade maior ou igual a 16 anos

print("Bem vindo ao curso de Python - Senac Barra da Tijuca RJ")
idade = int(input("Qual é a sua idade?"))

if (idade>=16):
    print("Você tem idade para realizar o curso de python")
else:
    print("Você não tem idade para realizar o curso de python")
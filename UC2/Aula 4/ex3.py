#Exercício 3 - Faça um programa que calcule o IMC do usuário e de a classificação conforme a tabela ao lado:

peso = float(input("Qual é o seu peso?"))
altura = float(input("Qual é a sua altura?"))

# Cálculo do IMC
imc = peso / (altura * altura)

#Classifica o print
classif = f"O seu imc é: {imc:.1f}. "

# Classifica os IMC com base nas condições física e Exibe as Recomendações
if (imc<18.5):
    print(classif + "A sua classificação é: Magreza. Grau de obesidade: 0")

elif (imc>=18.5 and imc<=24.9):
    print(classif + "A sua classificação é: Normal. Grau de obesidade: 0")

elif (imc>=25 and imc<=29.9):
    print(classif + "A sua classificação é: Sobrepeso. Grau de obesidade: 1")

elif (imc>=30 and imc<=39.9):
    print(classif + "A sua classificação é: Obesidade. Grau de Obesidade: 2")

elif (imc>=40):
    print(classif + "A sua classificação é: Obesidade grave. Grau de Obesidade: 3")

else:
    print("Não encontramos o seu cálculo de IMC e a sua classificação!")
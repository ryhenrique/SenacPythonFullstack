#Faça um programa para um lava rapido onde:

#1 - Lavagem Completa R$50.00
#2 - Lavagem Básica R$35.00

#Caso o usuário queira, o pretinho custa mais R$5.00

print("Bem-vindo ao Lava Rapido - SENAC RJ")

lavajato = int(input("1 - Lavagem Completa R$50.00\n2 - Lavagem Básica R$35.00\n"))
if lavajato == 1:

    lavagem = "Lavagem Completa"
    valortotal = 50
    print(f"Você selecionou a {lavagem}!")

elif lavajato == 2:

    lavagem = "Lavagem Básica"
    valortotal = 35
    print(f"Você selecionou a {lavagem}")

else:
    print("Você não selecionou a opção correta!")

pretinho = input("Você deseja adicionar o pretinho por R$5,00? (Sim ou Não?)")
if (pretinho == "sim"):
    valortotal += 5
    print(f"O valor total {valortotal}")
elif pretinho == "não" or "não":
    print(f"O serviço de {lavagem} será no total de R${valortotal} sem pretinho")
else:
    print(f"O serviço de {lavagem} será no total de RS${valortotal} com pretinho")
#Faça um programa que receba 1 numero e diga se ele é primo ou não.
#Peço um numero ao usuario
numero = int(input("Entre com um numero"))
#Uso uma variavel de apoio que definira se um numero é primo ou não
primo = True
#Faço um loop que vai do numero 2 até o numero antecessor a ele
for i in range(2,numero):
    #Se um numero for divisivel por qualquer numero sem ser 1 ou ele mesmo, primo será falso
    if(numero%i==0):
        primo = False
    #Se primo for falso, é porque ele é divisivel por mais algum numero sem ser 1 e ele mesmo
if (primo == False):
    print("Esse número não é primo")
else:
    print("Esse é um numero primo")
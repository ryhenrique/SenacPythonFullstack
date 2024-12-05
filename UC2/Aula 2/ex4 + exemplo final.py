#Peço a idade do usuário
print ("Qual sua idade?")
#Armazeno na variável
idade = int(input())
#Colocando o valor dos produtos
valor_calca_azul = 120
valor_jaqueta_verde = 150
#Colocando desconto no valor dos produtos
valor_com_desconto_calca_azul = valor_calca_azul - idade
valor_com_desconto_jaqueta_verde = valor_jaqueta_verde - idade
#Explicando para o usuário quais são os produtos e seus valores sem desconto
print (f"Na nossa loja temos os seguintes produtos: Calça azul com o valor {valor_calca_azul} e uma jaqueta verde com o valor {valor_jaqueta_verde}")
#Explicando para o usuário quais são os produtos e seus valores com desconto
print(f"Graças a sua idade, nos daremos um desconto de R${idade} para você nos dois produtos!")
print(f"A calça azul custará {valor_com_desconto_calca_azul} e a jaqueta custará {valor_com_desconto_jaqueta_verde}")
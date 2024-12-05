a = 1 
b = 1
pulo = 1

for i in range(10):
    print(a) 
    pulo = b - a # Atualiza 'pulo' com a distância entre os números
    temp = a     # Armazena o valor atual de 'a' em uma vari´vel temporária
    a = b        # Atualiza 'a' com o valor de 'b'
    b = temp + b # Atualiza 'b' com a soma do antigo 'a' e 'b'
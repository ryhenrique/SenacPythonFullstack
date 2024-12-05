usuario_pesokg = float(input("Coloque seu peso em KG:"))
usuario_metros = float(input("Coloque sua altura em metros:"))
imc = usuario_pesokg / ( usuario_metros * usuario_metros )
print(f"O seu imc é {imc:.1f}")
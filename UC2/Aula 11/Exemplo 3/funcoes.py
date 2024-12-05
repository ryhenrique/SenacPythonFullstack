# funcoes.py

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao programa."

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)
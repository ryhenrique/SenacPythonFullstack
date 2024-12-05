 # Conveter Celsius em Fahrenheit

def converter(celsius):
    return (celsius * 9 / 5 + 32)

celsius = float(input("Digite sua temperatura em Graus Celsius: "))
resultado = converter(celsius)
print(f"A temperatura de {celsius}° Celsius é equivalente a {resultado}° Fahrenheit")

# Converter Celsius em Kelvin
def converter(celsiustokelvin):
    return(celsiustokelvin + 273.15)
celsiustokelvin = float(input("Digite sua temperatura em Graus Celsius: "))
resultado = converter(celsiustokelvin)
print(f"a temperatura de {celsiustokelvin}° Celsius é equivalente a: {resultado} Kelvin")

# Converter Fahrenheit em Kelvin

def converter(fahrenheit):
    return(fahrenheit - 32) * 5/9 + 273.15
fahrenheit = float(input("Digite sua temperatura em ° Fahrenheit: "))
resultado = converter(fahrenheit)
print(f"A sua temperatura de {fahrenheit}° Fahrenheit é equivalente a: {resultado} Kelvin")
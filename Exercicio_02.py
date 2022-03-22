'''
Criar no repositório do git uma nova branch e subir nela um programa python contendo uma função qualquer
'''

def conversorCelsiusToFareinheit(temperaturaCelsius):
    temperaturaFareinheit = temperaturaCelsius * 1.8 + 32
    return temperaturaFareinheit

temperatura = float(input('Digite a temperatura em Celsius: '))

temperaturaConvertida = conversorCelsiusToFareinheit(temperatura)
print(f'Temperatura em Fareinheit: {temperaturaConvertida:.1f}°')
'''
Escreva um programa que recebe uma letra do usuário e diz se a letra foi uma vogal.
'''
letra = str(input('letra: ')).strip().lower()
if letra in "aeiou":
    print('É uma Vogal')
else:
    print('É uma Consoante')

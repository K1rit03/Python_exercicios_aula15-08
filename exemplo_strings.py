# STRINGS - sequencia ou lista de caracteres

texto = 'Exemplo de texto'
print(texto)

print(texto[0])

#percorrer caracteres de uma string

for caracter in texto:
    print(caracter)

#lowe - retorna uma copia uma string para minusculo

texto = 'Exemplo De Texto'
texto = texto.lower()
print(texto)

# upper - retorne uma copia da string convertida para maiusculo
texto ='Exemplo de Texto'
texto = texto.upper()
print(texto)

#tittle - Converte apenas a inicial da string em maiusculo
texto = 'exemplo de texto'
texto = texto.capitalize()
print(texto)

#strip - remove os espaços em branco do inicio e do final de uma string
texto = '          exemplo de texto'
textp = texto.strip()
print(texto)

#replace - substitui uma substring por outra substring
texto = texto.replace ('','-')
print(texto)

#index - retorna o indice de um determinado caracter
texto = 'exemplo de texto'
indice = texto.index ('texto')
print(indice)

#count - conta quantas vezes uma substring aparece na string
texto = 'exemplo de texto texto texto'
quantidade = texto.count('texto')
print(quantidade)

#split - divide uma string de acordo com um separador (retorna uma lista)
texto = 'exemplo de texto'
lista = texto.split(' ')
print(lista)

#in - verifica se uma substring existe em uma string
texto = 'exemplo de texto'
palavra = input('Digite um texto: ').upper()
if palavra in texto.upper():
    
    print('Existe')
else:
    print('Não existe')
def palindromo(texto):
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum)

    return texto_limpo == texto_limpo[::-1]


frase = input(" Digite uma palavra ou frase :")
resultado = palindromo(frase)

if resultado == True:
   resposta = 'Sim'
else:
    resposta = 'Não'

print(f"{frase} é um Palindromo?  {resposta}")
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

frase = "Python se tornou uma das linguagens de programação mais mais mais mais mais mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
print(palavras)

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
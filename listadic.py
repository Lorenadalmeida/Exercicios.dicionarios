#Exercicio 1
dic_aluno = [{"aluno":"Ryann", "idade":15, "nota": 9.8 }]
print(dic_aluno)
#exercicio 2
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print("Produto:", produto["nome"])
print("Estoque:", produto["estoque"])

#exercicio 3
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

#exercicio 4
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

#exercicio 5
contato = {"nome": "Ana", "email": "ana@email.com"}
print("telefone" in contato)

#exercicio 6 
def contar_palavras(lista):
    freq = {}
    for palavra in lista:
        freq[palavra] = freq.get(palavra, 0) + 1
    return freq

#exercicio 7
d = {"a": 1, "b": 2, "c": 3}
d_invertido = {valor: chave for chave, valor in d.items()}
print(d_invertido)

#exercicio 8 
notas_alunos = {
    "Lorena": [8, 9, 10],
    "Fred": [7, 6, 8],
    "Ryann": [9, 9, 10]}
print(notas_alunos)

#exercicio 9 
def mesclar_dicts(dic_1, dic_2):
    dic_3 = dic_1.copy()
    dic_3.update(dic_2) 
    return dic_3
dic_1 = {"Fred": 29, "Ryann": 15, "Lorena": 17}
dic_2 = {"Livros": 3, "sapatos": 4, "dicionarios": 3}
print(mesclar_dicts(dic_1, dic_2))

#exercicio 10 
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenado = dict(sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True))
print(ordenado)
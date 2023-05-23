# reduce - faz redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acumulador, produto):
#     print(acumulador)
#     print(produto)
#     print()
#     return acumulador + produto['preco']
# total = reduce(funcao_do_reduce, produtos, 0)

total = reduce(lambda ac, p: ac + p['preco'],
    produtos, 0)

print('Total é:', total)
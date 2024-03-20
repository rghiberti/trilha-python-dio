capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
nova_capacidade = (capacidade_atual * aumento_percentual // 100) + capacidade_atual
# TODO: Imprima a nova capacidade
print(nova_capacidade)
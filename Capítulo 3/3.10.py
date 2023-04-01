3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.

------------------------------------------------------------------------------------------

jogos = ['fortnite', 'csgo', 'brawlhalla', 'dota']
jogos[0] = 'lol'

jogos.append('fifa')
jogos.insert(0, 'dbd')

del jogos[-1]
jogos.pop(0)
jogos.remove('brawlhalla')

print(sorted(jogos))
jogos.sort()

jogos.reverse()

print('são os ' + str(len(jogos)) + ' melhores jogos')
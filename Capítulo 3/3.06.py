3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.

------------------------------------------------------------------------------------------

convidados = ['Einstein', 'Tesla', 'Darwin']

print('\n' + convidados[0] +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[1] +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[2].title() +', você está cordialmente convidado para um jantar.')

print("\n Avisamos aos convidados que foi encotrado uma mesa de jantar maior")

convidados.insert(0, 'von neumann')
convidados.insert(2, 'charles babbage')
convidados.append('ada lovelace')

print('\n' + convidados[0].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[1] +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[2].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[3] + ', você está cordialmente convidado para um jantar.')
print('\n' + convidados[4].title() + ', você está cordialmente convidado para um jantar.')
print('\n' + convidados[-1].title() + ', você está cordialmente convidado para um jantar.')
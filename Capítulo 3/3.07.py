3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa.

------------------------------------------------------------------------------------------

convidados = ['einstein', 'tesla', 'darwin']

print('\n' + convidados[0].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[1].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[2].title() +', você está cordialmente convidado para um jantar.')

print("\nAvisamos aos convidados que foi encotrado uma mesa de jantar maior.")

convidados.insert(0,'von neumann')
convidados.insert(2,'charles babbage')
convidados.append('ada lovelace')

print('\n' + convidados[0].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[1].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[2].title() +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[3].title() + ', você está cordialmente convidado para um jantar.')
print('\n' + convidados[4].title() + ', você está cordialmente convidado para um jantar.')
print('\n' + convidados[-1].title() + ', você está cordialmente convidado para um jantar.')

print("\ninfelizmente a mesa de jantar não chegará a tempo. Só podemos ter dois convidados.")

print('\n'+ convidados[0].title(), ', sinto muito, mas não posso convida-lo para o jantar.')
convidados.pop(0)

print('\n'+ convidados[0].title(), ', sinto muito, mas não posso convida-lo para o jantar.')
convidados.pop(0)

print('\n'+ convidados[0].title(), ', sinto muito, mas não posso convida-lo para o jantar.')
convidados.pop(0)

print('\n' + convidados[0].title(), ", sinto muito, mas não posso convida-lo para o jantar.")
convidados.pop(0)

print('\n'+ convidados[0].title(), ', ainda está convidado.')
print('\n'+ convidados[1].title(), ', ainda está convidado.')

del convidados[0]
del convidados[0]
print(convidados)
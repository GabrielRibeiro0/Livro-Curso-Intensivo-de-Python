3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.

------------------------------------------------------------------------------------------

convidados = ['Einstein', 'Tesla', 'Darwin']

print('\n' + convidados[2] +' não poderá comparecer por está em uma viagem')

convidados[2] = 'Elon musk'

print('\n' + convidados[0] +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[1] +', você está cordialmente convidado para um jantar.')
print('\n' + convidados[2].title() +', você está cordialmente convidado para um jantar.')
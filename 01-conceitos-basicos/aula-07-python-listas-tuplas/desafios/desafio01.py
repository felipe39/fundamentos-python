# Tupla com os meses do ano
meses = ( 'Janeiro', 'Fevereiro','Março','Abril', 'Maio', 'Junho', 'Junho',
'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',)

# Entrada da data de nascimento do usuário
data_nascimento = input("Digite sua data de nascimento: ")

# Fatiando e pegando o dia 0:2
dia = int(data_nascimento[0:2])

# Fatiando e pegando o indice exato entre e convertendo para Int
mes = int(data_nascimento[3:5])

#Ano 6:10
ano = int( data_nascimento[6:10])


print('\n',"-"*20)
print("Seu dia de nascimento é: ",dia)
print("Seu mês de nascimento é: ",meses[mes -1]) #Pega exatamente o mês na tupla
print("Seu ano de nascimento é: ",ano)
print("-"*20,"\n")
input("Digite ENTER para sair, ")

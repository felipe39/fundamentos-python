# Tupla contendo os meses do ano

meses = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
)

# Solicita a data de nascimento

data = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Obtém o mês digitado

mes = int(data[3:5])

# Exibe o mês correspondente

print("--------------------")
print("Seu mês de nascimento é:", meses[mes - 1])
print("--------------------")

input("\nDigite ENTER para sair.")

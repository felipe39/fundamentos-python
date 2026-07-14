#Entrada do peso das provas

peso1 = float(input("Peso da primeira prova: "))
peso2 = float(input("Peso da segunda prova: "))

#Entrada do peso das Notas
nota1 = float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))

#Calculo da média ponderada
media = ((peso1 * nota1) + (peso2 * nota2)) / (peso1 + peso2)

#Saída da média ponderada
print("\nAluno aprovado!")
print("Média:", round(media, 2))

#Apenas um comando para o usuário diditar ENTER para sair
input("\nPressione ENTER para sair.")

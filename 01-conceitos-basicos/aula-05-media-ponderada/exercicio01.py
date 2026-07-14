peso1 = float(input("Peso da primeira prova: "))
peso2 = float(input("Peso da segunda prova: "))

nota1 = float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))

media = ((peso1 * nota1) + (peso2 * nota2)) / (peso1 + peso2)

# "-" * 20 imprimi 20 vezes o "-" para separar os prints
print("\nResultado Final")
print("-" * 20)
print("Média:", round(media, 2))

input("\nPressione ENTER para sair.")

# Exercício 5: Situação do aluno
# Use if/elif/else para classificar a nota

nota = float(input("Digite a nota do aluno (0 a 100): "))

if nota == 100:
    print("Aprovado com excelência!")
elif nota >= 50:
    print("Aprovado.")
else:
    print("Reprovado.")


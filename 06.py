# Exercício 6: Desconto em ingresso
# Use operadores lógicos (and/or) para aplicar descontos

idade = int(input("Digite a sua idade: "))
carteira = input("Você possui carteira de estudante? (sim/nao): ").lower()

if idade < 12 or idade >= 60:
    print("Ingresso grátis! Você não paga.")
elif 12 <= idade <= 59 and carteira == "sim":
    print("Você paga meia entrada.")
else:
    print("Você paga o ingresso inteiro.")
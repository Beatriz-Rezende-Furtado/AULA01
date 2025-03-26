nota1=float(input("insira uma nota:"))
nota2=float(input("insira um nota: "))
div= (nota1 + nota2)/2
if div <= 5:
    print(f"reprovado média = {div}")
elif div >= 5 and div <=6.9:
    print(f"recuperação média = {div}")
else:
    print(f"passou média = {div}")
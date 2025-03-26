x=int(input("insira um numero:"))
y=int(input("insira um numero: "))
z=str(input("insira uma operação:"))
if z == "-":
    print(f"Resultado: {x - y}")
elif z == "+":
    print(f"Resultado: {x + y}")
elif z == "*":
    print(f"Resultado: {x * y}")
else:
    print(f"Resultado: {x / y}")


x=int(input("insira um numero: "))
y=int(input("insira um numero: "))
z=int(input("insira um numero: "))
if x > y and x > z:
    print(f"{x} é maior")
elif y > x and y > z:
    print(f"{y} é maior")
else:
    print(f"{z} é maior")
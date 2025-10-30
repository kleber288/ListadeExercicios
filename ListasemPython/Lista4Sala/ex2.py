import math
print("----Matriz fatorial----")
a = []
b = []
print("Entre com os valores de A:")
for i in range(6):
    a.append(int(input(f"entre com o {i+1} valor: ")))
    b.append(math.factorial(a[i]))
print("-------------")
print("Valores de B:")
print(b)
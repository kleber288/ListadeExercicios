print("----Invertendo matrizes----")
a = []
b = []
print("Entre com os valores da matriz A:")
for i in range(10):
    a.append(int(input(f"Entre com o {i+1} valor: ")))
print("-------------")
print("Valor da matriz B:")
a.reverse()
b = a
print(b)
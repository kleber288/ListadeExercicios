print("----Juntando matrizes----")
a = []
b = []
c = []
print("Entre com os valores da primeira matriz:")
for i in range(20):
    a.append(int(input(f"Entre com o {i+1} valor da matriz A: ")))
print("-------------")
print("Entre com os valores da segunda matriz:")
for i in range(30):
    b.append(int(input(f"Entre com o {i} da matriz B: ")))
print("-------------")
print("Valor da matriz C:")
c = a + b
print(c) 
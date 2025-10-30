print("----Subtração de matriz----")
a = []
b = []
c = []
print("Entre com os valores de A:")
for i in range(5):
    a.append(int(input(f"Entre com o {i+1} valor: ")))
print("-------------")
print("Entre com os valores de B:")
for i in range(5):
    b.append(int(input(f"Entre com o {i+1} valor: ")))
print("-------------")
for i in range(5):
    c.append(a[i]-b[i])
print("Valores de C:")
print(c)

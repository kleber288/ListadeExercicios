print("----Multiplicando vetores----")
a = []
b = []
print("Entre com os valores de A:")
for i in range(5):
    a.append(int(input(f"Entre com o {i+1} valor: "))) 
    b.append(a[i]*3) 
print("-------------")
print("Valores de B:")
for i in range(5):
    print(b[i])
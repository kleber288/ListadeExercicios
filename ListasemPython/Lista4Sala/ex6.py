print("----Quadrado de matrizes----")
a = []
b = []
print("matruiz A:")
for i in range(8):
    a.append(int(input(f"Entre com o {i+1} valor:")))
    b.append(a[i]**2)
print("-------------")
print("Matriz B:")
for i in range(8):
    print(f"O quadrado de {a[i]} é {b[i]}")
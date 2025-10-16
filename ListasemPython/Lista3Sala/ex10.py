print("----Somando numeros pares de 1 a 500----")
n = 0
i = 0
while i < 501:
    if i % 2 == 0:
        n = n + i
    i+=1
print(f"A soma total é {n}")
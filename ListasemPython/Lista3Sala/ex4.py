print("----Produto menor que 250----")
n = int(input("Entre com um numero menor ou igual a 50: "))
if n >= 1 and n <= 50:
    while n < 250:
        n = n * 3
        print(f"Valor de N: {n}")
else:
    print("Numero invalido!")
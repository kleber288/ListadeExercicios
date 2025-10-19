print("----Numeros divisiveis por 4 ou 5----")
n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("Entre comm o segundo numero: "))
if n1 % 4 == 0 or n1 % 5 == 0:
    print(f"{n1} é divisivel por 4 ou 5.")
else:
    print(f"{n1} não é divisivel por 4 ou 5.")
if n2 % 4 == 0 or n2 % 5 == 0:
    print(f"{n2} é divisivel por 4 ou 5.")
else:
    print(f"{n2} não é divisivel por 4 ou 5.")
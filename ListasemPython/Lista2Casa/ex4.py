print("----Maior, Menor e Meio----")
n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("Entre com o segundo numero: "))
n3 = int(input("Entre com o terceiro numero: "))
if n1 > n2 and n2 > n3:
    print(f"Maior numero: {n1}")
    print(f"Numero do meio: {n2}")
    print(f"Menor Numero: {n3}")
elif n1 > n3 and n3 > n2:
    print(f"Maior numero: {n1}")
    print(f"Numero do meio: {n3}")
    print(f"Menor Numero: {n2}")
elif n2 > n1 and n1 > n3:
    print(f"Maior numero: {n2}")
    print(f"Numero do meio: {n1}")
    print(f"Menor Numero: {n3}")
elif n2 > n3 and n3 > n1:
    print(f"Maior numero: {n2}")
    print(f"Numero do meio: {n3}")
    print(f"Menor Numero: {n1}")
elif n3 > n1 and n1 > n2:
    print(f"Maior numero: {n3}")
    print(f"Numero do meio: {n1}")
    print(f"Menor Numero: {n2}")
elif n3 > n2 and n2 > n1:
    print(f"Maior numero: {n3}")
    print(f"Numero do meio: {n2}")
    print(f"Menor Numero: {n1}")

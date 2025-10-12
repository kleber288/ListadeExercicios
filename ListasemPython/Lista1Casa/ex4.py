print("----Calculando Perimetro e Area----")
a = float(input("Digite o valor do lado A:"))
b = float(input("Digite o valor do lado B:"))
area = a*b
perimetro = 2*a + 2*b
if a == b:
    print("A area do quadrado é '%.2f'" %(area))
    print("O perimetro do quadrado é '%.2f'" %(perimetro))
else:
    print("A area do retangulo é '%.2f'" %(area))
    print("O perimetro do retangulo é '%.2f'" %(perimetro))
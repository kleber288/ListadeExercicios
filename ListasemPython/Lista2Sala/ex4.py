a = float(input("Digite o valor do lado A:"))
b = float(input("Digite o valor do lado B:"))
c = float(input("Digite o valor do lado C:"))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é Equilátero") 
    elif a == b or a == c or b == c:
        print("O triângulo é Isósceles")
    else:
        print("O triângulo é Escaleno")
else:
    print("Os valores fornecidos não formam um triângulo")

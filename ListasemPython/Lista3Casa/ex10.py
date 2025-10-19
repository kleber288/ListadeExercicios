print("----Calculadora basica----")
while 1:
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    print("s - Sair")
    escolha = input("Escolha uma opção: ")
    match escolha:
        case "+":
            a = float(input("Entre com o primeiro numero: "))
            b = float(input("Entre com o segundo  numero: "))
            result = a + b
            print(f"O resultado é {result}")
        case "-":
            a = float(input("Entre com o primeiro numero: "))
            b = float(input("Entre com o segundo  numero: "))
            result = a - b
            print(f"O resultado é {result}")
        case "*":
            a = float(input("Entre com o primeiro numero: "))
            b = float(input("Entre com o segundo  numero: "))
            result = a * b
            print(f"O resultado é {result}")
        case "/":
            a = float(input("Entre com o primeiro numero: "))
            b = float(input("Entre com o segundo  numero: "))
            result = a / b
            print(f"O resultado é {result}")
        case "s":
            break
print("Saindo...")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if (media >= 6.0):
    print("Parabens! Você foi aprovado com média '%.2f'"  %(media))
else:
    print("Infelizmente você não foi aprovado com média '%.2f'"  %(media))
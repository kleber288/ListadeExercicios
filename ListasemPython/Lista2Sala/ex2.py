nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print("Parabens! Você foi aprovado com media '%.2f'" %(media))
else:
    notaex = float(input("Digite a nota do exame:"))
    novamedia = (media + notaex) / 2
    if novamedia >= 5.0:
        print(f"Você foi aprovado em exame com média '%.2f" %(novamedia))
    else:
        print(f"Infelizmente você não foi aprovado com média '%.2f'" %(novamedia))
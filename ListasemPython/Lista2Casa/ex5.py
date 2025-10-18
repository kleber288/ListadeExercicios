print("----Calculo salario liquido----")
sbruto = float(input("digite o salario bruto: "))
htrabalha = int(input("Digite as horas trabalhadas: "))
if htrabalha > 160:
    htrabalha = htrabalha - 160
    adicionais = (sbruto / 160) + (htrabalha * 0.50)
    sbruto = sbruto + adicionais
if sbruto < 800.00:
    sliquido = sbruto
    print(f"O salario liquido é R$ {sliquido}")
elif sbruto >= 800.00 and sbruto <= 1600.00:
    sliquido = (sbruto - (sbruto * 0.13))
    print(f"O salario liquido é R$ {sliquido}")
else:
    sliquido = (sbruto - (sbruto * 0.22))
    print(f"O salario liquido é R$ {sliquido}")
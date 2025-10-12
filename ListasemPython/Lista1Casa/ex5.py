print("---Calculo do IMC---")
m = float(input("Seu peso em Kg:"))
h = float(input("Sua altura em metros:"))
imc = m / h**2
print("O valor do IMC é: '%.2f'" %(imc))
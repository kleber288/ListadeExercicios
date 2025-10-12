print("----Calculando metros----")
t = float(input("Digite o valor em segundos:"))
s0 = 2
v0 = 3
s = s0 + v0*t + 0.5 * 10 * t**2
print("O valor de metros será '%.2f'" %(s))
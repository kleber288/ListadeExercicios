print("----Calculando azulejos necessarios----")
ap = float(input("Digite a altura da parede:"))
lp = float(input("Digite a largura da parede:"))
areap = lp*ap
aa = float(input("Digite a altura do azulejo:"))
la = float(input("Digite a largura do azulejo:"))
areaa = aa*la
azune = areap / areaa
print("A quantidade de azulejos necessarios é '%.2f'" %(azune))
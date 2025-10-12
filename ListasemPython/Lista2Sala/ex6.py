import math
a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B"))
c = float(input("Digite o valor de C:"))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Os valores das raizes são '%.2f' e '%.2f'" %(x1, x2))
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    print("Os valores das duas raizes são '%.2f'" %(x1))
else:
    print("Não possui raizes")
    

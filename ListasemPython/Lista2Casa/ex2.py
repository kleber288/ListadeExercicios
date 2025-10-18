print("----Numero Chave----")
nc = 57
n = int(input("Entre com um numero entre 0 e 100:"))
r = n - 57
if r < 0:
    r = r*-1
    print("A distancia para o numero chave é", r)
elif r == 0:
    print("Voce acertou o numero chave!")
else:
    print("A distancia para o numero chave é", r)
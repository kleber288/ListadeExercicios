print("----Calculando media do bimestre----")
p1 = float(input("Digite o valor da nota da primeira avaliação:"))
p2 = float(input("Digite o valor da nota da segunda avaliação:"))
atv = float(input("Digite o valor da nota da atividade:"))
media = (p1*4 + p2*4 + atv*2) / 10
print("A media semestral do aluno foi: '%.2f'" %(media))
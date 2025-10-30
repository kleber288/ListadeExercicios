print("----Invertendo RA----")
ra = []
ran = []
for i in range(9):
    ra.append(int(input(f"Entre com o {i+1} algarismo do RA: ")))
    ran.append(ra[i])
print("-------------")
ran[0] = ra[1]
ran[1] = ra[0]
ran[8] = ra[7]
ran[7] = ra[8]
print("Antigo RA: ")
print(ra)
print("-------------")
print("Novo RA: ")
print(ran)
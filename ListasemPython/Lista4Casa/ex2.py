print("----Invertendo RA----")
ra = []
ran = []
for i in range(9):
    ra.append(int(input(f"Entre com o {i+1} algarismo do RA: ")))
    ran.append(ra[i])
print("-------------")
ran[5] = ra[8]
ran[6] = ra[7]
ran[7] = ra[6]
ran[8] = ra[5]
print("Antigo RA: ")
print(ra)
print("-------------")
print("Novo RA: ")
print(ran)
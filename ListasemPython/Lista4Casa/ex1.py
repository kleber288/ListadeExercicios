print("----Virus RAV----")
rav = []
rac = []
for i in range(9): 
    rav.append(int(input(f"Entre com o {i+1} algarismo do RAV: ")))
    rac.append(rav[i])
print("-------------")
rac[2] = rav[7]
rac[3] = rav[6]
rac[6] = rav[2]
rac[7] = rav[3]
print("Numero errado com o virus RAV: ")
print(rav )
print("-------------")
print("Numero certo do RAC: ")
print(rac)

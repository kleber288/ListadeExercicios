print("----Coddigo do curso----")
codcurso = int(input("Digite o numero do codigo: "))
if codcurso >= 1 and codcurso <= 5:
    match codcurso:
        case 1:
            print("Engenharia")
        case 2:
            print("Edificações")
        case 3:
            print("Sistemas Elétricos")
        case 4:
            print("Turismo")
        case 5:
            print("Análise de Sistemas")
else:
    print("Codigo invalido!")

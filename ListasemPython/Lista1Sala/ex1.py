print("-----Calculos da viagem-----")
tempo = float(input("digite o tempo gasto na viagem em minutos: "))
vel = float(input("digite a velocide media em km/h da viagem: "))
dist = (tempo/60) * vel
litros = dist/12
print("-----Dados da viagem-----")
print("Velocidade media:", vel ,"Km/h")
print("tempo gasto:", tempo/60 ,"Horas")
print("Ditancia percorrida:", dist ,"Km")
print("Quantidade de litros usada:", litros)
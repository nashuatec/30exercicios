#calculo idade em dias
idade = int(input("Digite quantos anos voce tem: "))
total = idade * 365
total_Horas = total * 24
total_minutos = total_Horas * 60
total_segundo = total_minutos * 60
print("voce tem: ",idade,"anos de idade, que equivale à: ",total,"dias vividos,e um total de :",total_Horas,"horas e: ",total_minutos,"minutos e um total de: ",total_segundo,"segundo de vida")

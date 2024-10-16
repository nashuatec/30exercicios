#conversao dias em semanas
dias = int(input("Digite o número de dias: "))
semanas = dias // 7
dias_restantes = dias % 7
print(f"{dias} dias correspondem a {semanas} semanas e {dias_restantes} dias.")

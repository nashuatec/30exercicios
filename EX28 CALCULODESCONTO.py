#calculo desconto progressivo
peca1 = float(input("Insira o valor da primeira peça: "))
peca2 = float(input("Insira o valor da segunda peça: "))
peca3 = float(input("Insira o valor da terceira peça: "))

valor_total = peca1+peca2+peca3
desconto1 = valor_total - (valor_total*0.05)
desconto2 = valor_total - (valor_total*0.10)
if valor_total >= 100:
    print("Valor total da sua compra era de: R$",valor_total,"reais ,com o desconto passa a ser de: R$ ",desconto1)
elif valor_total >= 500:
    print("Valor total da sua compra era de: R$",valor_total,"reais ,com o desconto passa a ser de: R$ ",desconto2)
else:
    print("Valor total da sua compra era de: R$",valor_total)
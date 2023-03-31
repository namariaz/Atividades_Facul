tipo_combustivel = input("Digite o tipo de combustível desejado (A = Álcool , G = Gasolina): ")
litros = float(input("Digite a quantidade de litros do combustível desejado: "))


if tipo_combustivel == 'A' and litros <= 20:
    print(f"Com {litros} litros você terá 3% de desconto, totalizando R${round((litros * 1.90) - (litros * 1.90) * 0.03, 2)} à ser pago")
else:
    if tipo_combustivel == 'A' and litros > 20:
        print(f"Com {litros} litros você terá 5% de desconto, totalizando R${round((litros * 1.90) - (litros * 1.90) * 0.05, 2)} à ser pago")
    else:
        if tipo_combustivel == 'G' and litros <= 20:
            print(f"Com {litros} litros você terá 4% de desconto, totalizando R${round((litros * 2.5) - (litros * 2.5) * 0.04, 2)} à ser pago")
        else:
            if tipo_combustivel == 'G' and litros > 20:
                print(f"Com {litros} litros você terá 6% de desconto, totalizando R${round((litros * 2.5) - (litros * 2.5) * 0.06, 2)} à ser pago")
            else:
                print("Tipo de combustível inválido!")
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input(f"Saldo disponível: R$ {saldo:.2f}.\n"
                            f"Informe o valor do saque: "))

        if valor > 0:
            if valor > saldo:
                print("Operação falhou! Saldo insuficiente.")

            elif valor > limite:
                print(f"Operação falhou! Limite para saque: R$ {limite:.2f}")

            elif numero_saques >= LIMITE_SAQUES:
                print(f"Operação falhou! Número máximo de saques excedido.")
            
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo disponível: R$ {saldo:.2f}")
        print("===============================================")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor selecione novamente a opção desejada.")

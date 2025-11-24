dados_lavoura = {}
while True:

    print('''█▀▀ ▄▀█ █▀█ █▀▄▀█ ▀█▀ █▀▀ █▀▀ █░█   █▀ █▀█ █░░ █░█ ▀█▀ █ █▀█ █▄░█ █▀
█▀░ █▀█ █▀▄ █░▀░█ ░█░ ██▄ █▄▄ █▀█   ▄█ █▄█ █▄▄ █▄█ ░█░ █ █▄█ █░▀█ ▄█''')

    print("\n1. Cadastrar Informações")
    print("2. Exibir Dados da Lavoura")
    print("3. Atualizar Informações")
    print("4. Remover Registro")
    print("5. Finalizar Sistema\n")

    op = int(input("Escolha uma opção: "))


    if op == 1:
        cultura = str(input("Escolha uma cultura (café ou tomate): ")).lower()

        if cultura == "tomate":
            comprimento = float(input("Digite o comprimento da área de plantio (m): "))
            largura = float(input("Largura do canteiro (m): "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
            area_tomate = comprimento * largura
            insumo_tomate = quantidade_por_metro * ruas
            dados_lavoura["tomate"] = {
                "comprimento": comprimento,
                "largura": largura,
                "area": area_tomate,
                "produto": produto,
                "quantidade_por_metro": quantidade_por_metro,
                "ruas": ruas,
                "insumo_total": insumo_tomate
            }


        elif cultura == 'café':
            raio = float(input("Digite o raio do circulo: "))
            produto = input("Digite o produto a ser aplicado: ")
            quantidade_por_metro = float(input("Digite a quantidade por metro (em mL): "))
            ruas = int(input("Digite o número de ruas: "))
            area_cafe = 3.14 * (raio ** 2)
            insumo_cafe = quantidade_por_metro * ruas
            dados_lavoura["café"] = {
                "raio": raio,
                "area": area_cafe,
                "produto": produto,
                "quantidade_por_metro": quantidade_por_metro,
                "ruas": ruas,
                "insumo_total": insumo_cafe
            }
        else:
            print("Cultura invalida! Tente novamente")
            continue

        print("Dados inseridos com sucesso!")


    elif op == 2:
        if not dados_lavoura:
            print("Nenhuma informação cadastrada ainda!")
            continue

        cultura_escolhida = input("Escolha uma cultura para exibir (café ou tomate): ").lower()
        if cultura_escolhida in dados_lavoura:
            print(f"\nDados da cultura {cultura_escolhida}:")
            print(f"Área: {dados_lavoura[cultura_escolhida]['area']:.2f} m²")
            print(f"Produto aplicado: {dados_lavoura[cultura_escolhida]['produto']}")
            print(f"Total de insumo necessário: {dados_lavoura[cultura_escolhida]['insumo_total']:.2f} mL")
        else:
            print("Cultura não cadastrada!")

    elif op == 3:
        cultura = input("Digite a cultura que deseja atualizar (café ou tomate): ").lower()
        if cultura in dados_lavoura:
            if cultura == "tomate":
                comprimento = float(input("Digite o novo comprimento da área de plantio (m): "))
                largura = float(input("Digite a nova largura do canteiro (m): "))
                quantidade_por_metro = float(input("Digite a nova quantidade por metro (em mL): "))
                ruas = int(input("Digite o novo número de ruas: "))
                dados_lavoura[cultura]["comprimento"] = comprimento
                dados_lavoura[cultura]["largura"] = largura
                dados_lavoura[cultura]["area"] = comprimento * largura
                dados_lavoura[cultura]["quantidade_por_metro"] = quantidade_por_metro
                dados_lavoura[cultura]["ruas"] = ruas
                dados_lavoura[cultura]["insumo_total"] = quantidade_por_metro * ruas
            elif cultura == "café":
                raio = float(input("Digite o novo raio do círculo: "))
                quantidade_por_metro = float(input("Digite a nova quantidade por metro (em mL): "))
                ruas = int(input("Digite o novo número de ruas: "))
                dados_lavoura[cultura]["raio"] = raio
                dados_lavoura[cultura]["area"] = 3.14 * (raio ** 2)
                dados_lavoura[cultura]["quantidade_por_metro"] = quantidade_por_metro
                dados_lavoura[cultura]["ruas"] = ruas
                dados_lavoura[cultura]["insumo_total"] = quantidade_por_metro * ruas
            print("Dados atualizados com sucesso!")
        else:
            print("Cultura não cadastrada!")


    elif op == 4:
        cultura = input("Deseja apagar qual cultura? (café ou tomate): ").lower()
        if cultura in dados_lavoura:
            del dados_lavoura[cultura]
            print("Dados removidos com sucesso!")
        else:
            print("Cultura não encontrada!")

    elif op == 5:
        print("Finalizando sistema")
        break

    else:
        print("Opção inválida. Tente Novamente!")






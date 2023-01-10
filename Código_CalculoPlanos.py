musc = [1731.4, 953.4, 189.9]
colet = [1868.9, 1019.4, 189.9]
nat1x = [2418.9, 1439.4, 269.9]
nat2x = [3298.9, 1919.4, 349.9]
nat3x = [3848.9, 2219.4, 399.9]
hidr2x = [2198.9, 1319.4, 249.9]
hidr3x = [2968.9, 1799.4, 339.9]
pilates1x = [2308.9, 1386.0, 249.9]
pilates2x = [3628.9, 2189.4, 419.9]
array_modalidades = [musc, colet, nat1x, nat2x,
                     nat3x, hidr2x, hidr3x, pilates1x, pilates2x]
array_nomes_modalidades = ["Musculação", "Aulas coletivas", "Natação 1x/sem", "Natação 2x/sem", "Natação 3x/sem",
                           "Hidroginastica 2x/sem", "Hidroginastica 3x/sem", "Pilates em estúdio 1x/sem", "Pilates em estúdio 2x/sem"]

primeira_modalidade = [0.0, 0.0, 0.0]
segunda_modalidade = [0.0, 0.0, 0.0]
terceira_modalidade = [0.0, 0.0, 0.0]

nome_primeira_modalidade = ""
nome_segunda_modalidade = ""
nome_terceira_modalidade = ""


def duas_modalidades():
    print(
        "Insira o número da primeira modalidade: \n[1] Musculação \n[2] Aulas coletivas\n[3] Natação 1x/sem\n[4] "
        "Natação 2x/sem\n[5] Natação 3x/sem\n[6] Hidro 2x/sem\n[7] Hidro 3x/sem\n[8] Pilates 1x/sem\n[9] Pilates 2x/sem")

    tmp = int(input("Número da primeira modalidade escolhida: "))
    primeira_modalidade = array_modalidades[tmp-1]
    nome_primeira_modalidade = array_nomes_modalidades[tmp-1]
    tmp = int(input("Número da primeira modalidade escolhida: "))
    segunda_modalidade = array_modalidades[tmp-1]
    nome_segunda_modalidade = array_nomes_modalidades[tmp-1]

    if segunda_modalidade > primeira_modalidade:
        tmp = nome_segunda_modalidade
        nome_segunda_modalidade = nome_primeira_modalidade
        nome_primeira_modalidade = tmp

    print("\n\n\n            Texto para o cliente: \n")

    # criar lista final baseado em sort individual dos 3 elementos da primeira_moalidade, segunda_modalidade

    lista_menor = [0, 0, 0]
    lista_maior = [1, 1, 1]

    if primeira_modalidade[0] > segunda_modalidade[0]:
        lista_maior[0] = primeira_modalidade[0]
        lista_menor[0] = segunda_modalidade[0]
    else:
        lista_maior[0] = segunda_modalidade[0]
        lista_menor[0] = primeira_modalidade[0]

    if primeira_modalidade[1] > segunda_modalidade[1]:
        lista_maior[1] = primeira_modalidade[1]
        lista_menor[1] = segunda_modalidade[1]
    else:
        lista_maior[1] = segunda_modalidade[1]
        lista_menor[1] = primeira_modalidade[1]

    if primeira_modalidade[2] > segunda_modalidade[2]:
        lista_maior[2] = primeira_modalidade[2]
        lista_menor[2] = segunda_modalidade[2]
    else:
        lista_maior[2] = segunda_modalidade[2]
        lista_menor[2] = primeira_modalidade[2]

    lista_final = [lista_maior, lista_menor]

    # print(lista_final)

    total_mensal = lista_final[0][2] + (0.55 * lista_final[1][2])
    print("Primeira modalidade:", nome_primeira_modalidade, "\n*Segunda modalidade:*", nome_segunda_modalidade +
          "\n\n*Mensalidade recorrente*\nModalidade de maior valor: R$ " +
          str(round(lista_final[0][2], 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][2], 2)),
          "por R$ " + str(round((lista_final[1][2] * 0.55), 2)) + "\nTotal: R$ " + str(round(total_mensal, 2)) + "/mês\n")

    total_semestral = lista_final[0][1] + (0.55 * lista_final[1][1])
    print("Semestralidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][1], 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][1], 2)),
          "por R$ " + str(round((lista_final[1][1] * 0.55), 2)) + "\nTotal: R$ " + str(round(total_semestral, 2)) +
          ", em até 6x de R$ " + str(round(total_semestral / 6, 2)) + "\n")

    total_anual = lista_final[0][0] + (0.55 * lista_final[1][0])
    print("Anualidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][0], 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][0], 2)),
          "por R$ " + str(round((lista_final[1][0] * 0.55), 2)) + "\nTotal: R$ " + str(round(total_anual, 2)) +
          ", em até 11x de R$ " + str(round(total_anual / 11, 2)) + "\n")

    print("\n\n            E em caso de plano familiar, mandar este: \n")

    total_mensal = lista_final[0][2] + (0.55 * lista_final[1][2])
    print("Primeira modalidade:", nome_primeira_modalidade, "\n*Segunda modalidade:*", nome_segunda_modalidade +
          "\n\n*Mensalidade recorrente*\nModalidade de maior valor: R$ " +
          str(round(lista_final[0][2] * 0.915, 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][2], 2)),
          "por R$ " + str(round((lista_final[1][2] * 0.55) * 0.915, 2)) + "\nTotal: R$ " + str(round(total_mensal * 0.915, 2)) + "/mês\n")

    total_semestral = lista_final[0][1] + (0.55 * lista_final[1][1])
    print("Semestralidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][1] * 0.915, 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][1], 2)),
          "por R$ " + str(round((lista_final[1][1] * 0.55) * 0.915, 2)) + "\nTotal: R$ " + str(round(total_semestral * 0.915, 2)) +
          ", em até 6x de R$ " + str(round((total_semestral / 6) * 0.915, 2)) + "\n")

    total_anual = lista_final[0][0] + (0.55 * lista_final[1][0])
    print("Anualidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][0] * 0.915, 2)),
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][0], 2)),
          "por R$ " + str(round((lista_final[1][0] * 0.55) * 0.915, 2)) + "\nTotal: R$ " + str(round(total_anual * 0.915, 2)) +
          ", em até 11x de R$ " + str(round((total_anual / 11) * 0.915, 2)) + "\n")


def tres_modalidades():
    print("Insira o número da primeira modalidade: \n[1] Musculação \n[2] Aulas coletivas\n[3] Natação 1x/sem\n[4] "
          "Natação 2x/sem\n[5] Natação 3x/sem\n[6] Hidro 2x/sem\n[7] Hidro 3x/sem\n[8] Pilates 1x/sem\n[9] Pilates 2x/sem")

    tmp = int(input("Número da primeira modalidade escolhida: "))
    primeira_modalidade = array_modalidades[tmp-1]
    nome_primeira_modalidade = array_nomes_modalidades[tmp-1]
    tmp = int(input("Número da primeira modalidade escolhida: "))
    segunda_modalidade = array_modalidades[tmp-1]
    nome_segunda_modalidade = array_nomes_modalidades[tmp-1]
    tmp = int(input("Número da primeira modalidade escolhida: "))
    terceira_modalidade = array_modalidades[tmp-1]
    nome_terceira_modalidade = array_nomes_modalidades[tmp-1]

    # Typedef de valor e nome da modalidade.
    # Array com esses 3 typedefs
    # Colocar o array em ordem e atribuir nome_primeira_modalidade = array.nome[0]

    print("\n\n\n            Texto para o cliente: \n")

    # criar lista final baseado em sort individual dos 3 elementos da primeira_moalidade, segunda_modalidade

    lista_menor = [0, 0, 0]
    lista_media = [1, 1, 1]
    lista_maior = [2, 2, 2]

    lista_tmp = [0, 0, 0]

    lista_tmp = [primeira_modalidade[0],
                 segunda_modalidade[0], terceira_modalidade[0]]
    lista_tmp.sort()  # De menor para maior ; Anualidades
    lista_menor[0] = lista_tmp[0]
    lista_media[0] = lista_tmp[1]
    lista_maior[0] = lista_tmp[2]

    lista_tmp = [primeira_modalidade[1],
                 segunda_modalidade[1], terceira_modalidade[1]]
    lista_tmp.sort()  # De menor para maior ; Semestralidades
    lista_menor[1] = lista_tmp[0]
    lista_media[1] = lista_tmp[1]
    lista_maior[1] = lista_tmp[2]

    lista_tmp = [primeira_modalidade[2],
                 segunda_modalidade[2], terceira_modalidade[2]]
    lista_tmp.sort()  # De menor para maior ; Mensalidades
    lista_menor[2] = lista_tmp[0]
    lista_media[2] = lista_tmp[1]
    lista_maior[2] = lista_tmp[2]

    lista_final = [lista_maior, lista_media, lista_menor]
    # lista_final[x][y]
    # x = Lista maior, media e menor
    # y = Anual, semestral e mensal

    # lista_final[x][2]
    total_mensal = lista_final[0][2] + (0.55 * lista_final[1][2])
    print("Modalidades desejadas:\n", nome_primeira_modalidade, "\n", nome_segunda_modalidade,
          "\n", nome_terceira_modalidade +
          "\n\n*Mensalidade recorrente*\nModalidade de maior valor: R$ " + str(round(lista_final[0][2], 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][2], 2)),
          "por R$" + str(round((lista_final[1][2] * 0.55),
                               2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][2], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(
            round(total_mensal, 2)) + "/mês\n")

    total_semestral = lista_final[0][1] + (0.55 * lista_final[1][1])
    print("Semestralidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][1], 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][1], 2)),
          "por R$ " + str(round((lista_final[1][1] * 0.55),
                                2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][1], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(round(total_semestral, 2)) +
          ", em até 6x de R$" + str(round(total_semestral / 6, 2)) + "\n")

    total_anual = lista_final[0][0] + (0.55 * lista_final[1][0])
    print("Anuaidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][0], 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][0], 2)),
          "por R$ " + str(round((lista_final[1][0] * 0.55),
                                2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][0], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(round(total_anual, 2)) +
          ", em até 11x de R$" + str(round(total_anual / 11, 2)) + ".\n")

    print("\n\n            E em caso de plano familiar, mandar este: \n")

    total_mensal = lista_final[0][2] + (0.55 * lista_final[1][2])
    print("Modalidades desejadas:\n", nome_primeira_modalidade, "\n", nome_segunda_modalidade,
          "\n", nome_terceira_modalidade +
          "\n\n*Mensalidade recorrente*\nModalidade de maior valor: R$ " + str(round(lista_final[0][2] * 0.915, 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][2], 2)),
          "por R$" + str(round((lista_final[1][2] * 0.55) * 0.915,
                               2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][2], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(
            round(total_mensal * 0.915, 2)) + "/mês\n")

    total_semestral = lista_final[0][1] + (0.55 * lista_final[1][1])
    print("Semestralidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][1] * 0.915, 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][1], 2)),
          "por R$ " + str(round((lista_final[1][1] * 0.55) * 0.915,
                                2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][1], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(round(total_semestral * 0.915, 2)) +
          ", em até 6x de R$" + str(round((total_semestral / 6) * 0.915, 2)) + "\n")

    total_anual = lista_final[0][0] + (0.55 * lista_final[1][0])
    print("Anuaidade\nModalidade de maior valor: R$ " + str(round(lista_final[0][0] * 0.915, 2)) +
          "\nSegunda modalidade: de R$ " + str(round(lista_final[1][0], 2)),
          "por R$ " + str(round((lista_final[1][0] * 0.55) * 0.915,
                                2)) + "\nTerceira modalidade (sem custo adicional): de R$ " + str(
              round(lista_final[2][0], 2)), "por R$ 00.00"
          + "\nTotal: R$ " + str(round(total_anual * 0.915, 2)) +
          ", em até 11x de R$" + str(round((total_anual / 11) * 0.915, 2)) + ".\n")


qtd_modalidades = input("Quantas modalidades seriam? ")

if int(qtd_modalidades) == 2:
    duas_modalidades()

if int(qtd_modalidades) == 3:
    tres_modalidades()

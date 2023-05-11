partidoA = []
partidoB = []
partidoC = []

def urna():
    while True:
        inicial = input("Urna Eletrônica\nPartidoA [10]\nPartidoB [11]\nPartidoC [12]\nSelecione o número do partido (0 para sair): ")

        if inicial == '10':
            candidatoA = input("Você escolheu o PartidoA. Digite '1' para confirmar o voto ou '0' para voltar ao início: ")

            if candidatoA == '1':
                print("Voto confirmado com sucesso")
                voto = 1
                partidoA.append(voto)
                print(partidoA)

        elif inicial == '11':
            candidatoB = input("Você escolheu o PartidoB. Digite '1' para confirmar o voto ou '0' para voltar ao início: ")

            if candidatoB == '1':
                print("Voto confirmado com sucesso")
                voto = 1
                partidoB.append(voto)
                print(partidoB)

        elif inicial == '12':
            candidatoC = input("Você escolheu o PartidoC. Digite '1' para confirmar o voto ou '0' para voltar ao início: ")

            if candidatoC == '1':
                print('Voto confirmado com sucesso')
                voto = 1
                partidoC.append(voto)
                print(partidoC)

        elif inicial == '0':
            break

        if sum(partidoA) == 20:
            print("PartidoA venceu as eleições!")
            break

        elif sum(partidoB) == 20:
            print("PartidoB venceu as eleições!")
            break

        elif sum(partidoC) == 20:
            print("PartidoC venceu as eleições!")
            break

urna()

import dados
import time
import playsound

print("Quem será o meu amigo(a) secreto(a)?")
time.sleep(1)


def main():
    quem_foi = []
    numeros_ja_escolhidos = []
    tentativas = 0
    max_tentativas = 10
    while True:
        try:
            numero = int(input("Escolha o número de uma dica (1-6): "))
            if numero < 1 or numero > 6:
                print("Número inválido. Por favor, escolha um número entre 1 e 6.")
                continue
            if numero in numeros_ja_escolhidos:
                print('Esse número já foi escolhido')
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue
        numeros_ja_escolhidos.append(numero)
        time.sleep(1)
        print(dados.dicas(numero))
        time.sleep(1)
        tentativa = input('Quem você acha que é?: ').title()
        time.sleep(1)
        if tentativa != dados.resposta():
            print(f'NÃO FOI DESSA VEZ, {tentativa} não é meu amigo(a) secreto(a!')
            playsound.playsound("wrong-answer-buzzer.mp3")
            quem_foi.append(tentativa)
            print(f'Você ja tentou {quem_foi}')
            tentativas += 1
            if tentativas == max_tentativas:
                print("Você atingiu o número máximo de tentativas. Melhor sorte na próxima vez!")
                break
        if tentativa == dados.resposta():
            print(f"Parabéns, o meu amigo(a) secreto(a) é {dados.resposta()}")
            playsound.playsound("ja-ganhou-tantantan.mp3")
            break


if __name__ == "__main__":
    main()

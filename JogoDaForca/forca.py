import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de forca da Grazi")
    print("***********************************")

    #vamos chamar a palavra
    palavra_secreta = carregar_palavra_secreta()

    #mostrar as nossas letras, vetor com letras que acertamos, tem que ser do tamanho da palavra secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    #criar variáveis para termos controle
    enforcou = False
    acertou = False
    erros = 0

    #vamos mostrar as letras acertadas
    print(letras_acertadas)

    #fazer um while para ver se acertamos ou erramos
    while(not enforcou and not acertou):
        chute = input("Qual é a letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            marcar_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print(f"Você errou {erros} de 7 tentativas!")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns! Você ganhou!")
    else:
        print(f"Você perdeu! A palavra era {palavra_secreta}")

# criar método para carregar palavra secreta
def carregar_palavra_secreta():
    #informar caminho e o que iremos fazer com o arquivo = "r" read
    arquivo = open("D:/aArquivosOrganizados/Dev/Projetos/Python/JogoDaForca/palavras.txt", "r")
    #criar um array aonde salvaremos as palavras
    palavras = []

    #faremos um for para ler as palavras do arquivo e adicionar no array
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    #fechar arquivo
    arquivo.close()

    #pegar aleatoriamente as palavras - vamos pegar um número aleatório
    numero = random.randrange(0, len(palavras))
    #desse número aleatório vamos escolher uma posição do vetor
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        
        index += 1

jogar()
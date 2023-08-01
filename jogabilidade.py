from batalha import batalhar
from loja import barganhar

def escolherAcao(guarda, personagem):
    print("Escolha o que você quer fazer?")
    print(f"[1] - Batalha com o guarda nº {guarda}")
    print("[2] - Entrar na loja")

    escolha = int(input())
    if (escolha == 1):
        # que pra batalha é importe também passar 
        # o guarda envolvido / o inimigo
        personagem = batalhar(personagem)
    elif (escolha == 2):
        personagem = barganhar(personagem)

    return personagem



def PassarPelosGuardas(quantidadeGuardas, personagem):
    for guarda in range(quantidadeGuardas):
        numeroDoGuarda = guarda + 1
        personagem = escolherAcao(numeroDoGuarda, personagem)
    
    return (quantidadeGuardas, personagem)

    
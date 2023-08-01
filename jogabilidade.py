from batalha import batalhar
from loja import barganhar

def escolherAcao(guarda, personagemSePreprando):
    print("Escolha o que você quer fazer?")
    print(f"[1] - Batalha com o guarda nº {guarda}")
    print("[2] - Entrar na loja")

    escolha = int(input())
    if (escolha == 1):
        personagemSePreprando = batalhar(personagemSePreprando)
    elif (escolha == 2):
        personagemSePreprando = barganhar(personagemSePreprando)
    return personagemSePreprando



def PassarPelosGuardas(quantidadeGuardas, personagem):
    for guarda in range(quantidadeGuardas):
        numeroDoGuarda = guarda + 1
        personagem = escolherAcao(numeroDoGuarda, personagem)
    
    return (quantidadeGuardas, personagem)

    
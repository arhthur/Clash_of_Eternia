from batalha import batalhar
from loja import barganhar

personagem = {
    "nome": "Mario",
    "dinheiro": 30,
    "stamina": 50,
    "bolsa": [],
    "equipamento": []
}

quantidadeGuardas = 7

print("Boas vindas ao seu pior pesadelo, está na hora de provar que você não é um mediocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {quantidadeGuardas} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida mediocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")


print("Escolha o que você quer fazer?")
print("[1] - Batalha com o guarda nº 1")
print("[2] - Entrar na loja")

escolha = int(input())
if (escolha == 1):
    personagem = batalhar(personagem)
elif (escolha == 2):
    personagem = barganhar(personagem)
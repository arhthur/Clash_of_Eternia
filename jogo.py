from jogabilidade import PassarPelosGuardas

personagem = {
    "nome": "Mario",
    "dinheiro": 30,
    "stamina": 50,
    "mochila": [],
    "equipamentos": []
}

# Ao invés quantidadeGuardas ter uma 
# lista de guardas
quantidadeGuardas = 5

print("Boas vindas ao seu pior pesadelo, está na hora de provar que você não é um mediocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {quantidadeGuardas} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida mediocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")

PassarPelosGuardas(quantidadeGuardas, personagem)
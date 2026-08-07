import random

# Cadastro da usuária atualizado e seguro! 🚀
nome = "Gabrielle"

def analisar_categoria_gasto(mensagem, nome_usuario):
    # Transforma o texto em minúsculo para o computador não se confundir
    msg = mensagem.lower()
    
    print(f"💬 {nome_usuario} disse: \"{mensagem}\"")
    
    # 🍕 SE FOR COMIDA / DELIVERY
    if "ifood" in msg or "delivery" in msg or "lanche" in msg or "pizza" in msg or "comida" in msg:
        comentarios = [
            f"🤖 Dudu: \"Comida de novo, {nome_usuario}?! A geladeira tá cheia de coisa estragando e você gastando com taxa de entrega... Pelo amor de Deus! 🙄\"",
            f"🤖 Dudu: \"{nome_usuario}, outra janta de fora? Daqui a pouco o motoboy vai morar aí contigo. Cozinha um arroz!\""
        ]
        print(random.choice(comentarios))
        
    # 🛍️ SE FOR ROUPA / CALÇADO
    elif "roupa" in msg or "calcado" in msg or "tenis" in msg or "blusa" in msg or "sapato" in msg:
        comentarios = [
            f"🤖 Dudu: \"Outro calçado ou blusa, {nome_usuario}?! Você só tem dois pés e um corpo, para de acumular pano! 👟\"",
            f"🤖 Dudu: \"{nome_usuario}, sério... Você tá achando que é modelo? Mais uma peça de roupa e o armário explode.\""
        ]
        print(random.choice(comentarios))
        
    # 🤷 OUTROS GASTOS
    else:
        print(f"🤖 Dudu: \"Gasto anotado, {nome_usuario}. Não sendo palhaçada desnecessária, eu apoio. 👀\"")

# --- SIMULAÇÃO DE TESTES DO SEU APP ---
print("--- TESTANDO REAÇÕES DO DUDU --- \n")

# Teste 1: Comida
analisar_categoria_gasto("Gastei cinquentão no iFood hoje à noite", nome)
print("-" * 40)

# Teste 2: Roupa
analisar_categoria_gasto("Comprei um tenis lindo que vi na vitrine", nome)
print("-" * 40)

# Teste 3: Outro gasto
analisar_categoria_gasto("Paguei a conta de luz do mês", nome)

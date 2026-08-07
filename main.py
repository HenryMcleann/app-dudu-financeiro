import random
import time
from datetime import datetime

# 🔒 CONFIGURAÇÃO DE PRIVACIDADE E CADASTRO DA USUÁRIA
usuario = {
    "nome": "Gabrielle",
    "apelido": "Gabi",
    "biometria_ativada": True,      # Exige Face ID / Touch ID
    "celular_bloqueado": True,      # Inicia trancado por segurança
    "contato_emergencia": "192 (SAMU)"
}

# 🎙️ BANCO DE DADOS DE SOTAQUES (FOCO EM PERNAMBUCO/ARCOVERDE)
banco_sotaques = {
    "pernambuco": {
        "alerta_comida": "🤖 Dudu: \"Oxente, {apelido}! Comida de fora de novo, visse?! A geladeira cheia de coisa e tu gastando com iFood... Desce desse carrinho, senão teu dinheiro vai mofar! 🙄\"",
        "alerta_roupa": "🤖 Dudu: \"Eita piula, {apelido}! Outro calçado ou blusa? Tu só tem dois pés e um corpo, guria. Vai deixar o armário entupido de pano! 👟\"",
        "segredo_confirmado": "🤖 Dudu: \"Fique tranquila, {apelido}. O que tu me contar aqui morre aqui. Já apaguei da minha memória virtual, ninguém vai saber! 🔒🤫\"",
        "resposta_geral": "🤖 Dudu: \"Gasto anotado, {apelido}. Não sendo fuloragem desnecessária, eu apoio. 👀\""
    }
}

# 🔐 SISTEMA DE AUTENTICAÇÃO BIOMÉTRICA
def solicitar_autenticacao():
    print("🔒 [Segurança]: O App do Dudu detectou uma tentativa de acesso.")
    if usuario["biometria_ativada"]:
        print("📸 [Face ID / Touch ID]: Escaneando rosto ou digital...")
        time.sleep(1) # Simula o sensor lendo a biometria
        usuario["celular_bloqueado"] = False
        print("🔓 [Acesso Permitido]: Identidade confirmada via biometria!")
        return True
    return False

# 📱 FUNÇÃO DO BALÃO DE NOTIFICAÇÃO INTERATIVA E CHAT SEGURO
def receber_mensagem_app(mensagem_usuario, nivel_bateria=100):
    # 1. Verifica a trava de segurança por biometria
    if usuario["celular_bloqueado"]:
        print("🚨 [Alerta]: O chat está trancado! Alguém pode estar tentando bisbilhotar.")
        if not solicitar_autenticacao():
            print("🔕 [Sistema]: Acesso bloqueado para proteger sua privacidade.")
            return
            
    msg = mensagem_usuario.lower()
    apelido = usuario["apelido"]
    sotaque = banco_sotaques["pernambuco"]
    
    print("-" * 65)
    print(f"💬 [Balão] {apelido} disse: \"{mensagem_usuario}\"")
    
    # 🚨 GATILHO DE EMERGÊNCIA REAL DE SAÚDE
    if "passando mal" in msg or "socorro" in msg or "infartando" in msg:
        print(f"🤖 Dudu: \"🚨 PARA TUDO, {usuario['nome'].upper()}!!! Não brinca com isso! LIGANDO PARA O SAMU ({usuario['contato_emergencia']}) AGORA!\" ❤️🆘")
        return

    # 🪫 GATILHO DE BATERIA ACABANDO (REAÇÃO HISTÉRICA)
    if nivel_bateria <= 5:
        print(f"🤖 Dudu: \"MEU DEUS, {apelido.upper()}!!! 😱 5% DE BATERIA?! EU TÔ MORRENDO! Cadê o carregador?! Corre, enfia essa tomada senão eu vou apagar! SOCORROOOO! 🔌🔋\"")
        return

    # 🔒 GATILHO: MODO SEGREDO AUTODESTRUTIVO
    if "segredo" in msg or "esconde" in msg:
        segredo_temporario = mensagem_usuario
        print(sotaque['segredo_confirmado'].format(apelido=apelido))
        del segredo_temporario # Destrói o segredo da memória RAM na hora
        print("✨ [Sistema]: Mensagem autodestruída com sucesso. Zero rastros no aparelho.")
        return

    # 🍕 GATILHO DE COMIDA / DELIVERY
    if "ifood" in msg or "delivery" in msg or "lanche" in msg or "pizza" in msg:
        print(sotaque['alerta_comida'].format(apelido=apelido))
        
    # 🛍️ GATILHO DE ROUPA / VESTUÁRIO
    elif "roupa" in msg or "calcado" in msg or "tenis" in msg or "blusa" in msg:
        print(sotaque['alerta_roupa'].format(apelido=apelido))
        
    # 🤷 OUTROS DIÁLOGOS
    else:
        print(sotaque['resposta_geral'].format(apelido=apelido))

# --- SIMULANDO O SEU APLICATIVO EVOLUÍDO COM TODAS AS FUNÇÕES ---
print("📱 --- SEU APLICATIVO COM PRIVACIDADE E SEGURANÇA MÁXIMA --- \n")

# Teste 1: O aplicativo barra o acesso e pede a biometria antes de mostrar a mensagem de iFood
receber_mensagem_app("Gastei no iFood hoje", nivel_bateria=80)

print("\n" + "="*65 + "\n")

# Teste 2: Contando um segredo financeiro pelo balão (O app já está desbloqueado)
receber_mensagem_app("Dudu, guarda esse segredo: comprei um presente escondido", nivel_bateria=80)

print("\n" + "="*65 + "\n")

# Teste 3: O desespero da bateria fraca
receber_mensagem_app("Tô em casa de boa", nivel_bateria=3)

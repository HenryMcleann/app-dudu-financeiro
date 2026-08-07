import random
import time

# 🔒 CONFIGURAÇÃO DE PRIVACIDADE E CADASTRO DO USUÁRIO
usuario = {
    "nome": "Henrique",
    "apelido": "Henrique",  # Dudu vai te chamar pelo seu nome real
    "biometria_ativada": True,      
    "celular_bloqueado": True,      
    "contato_emergencia": "192 (SAMU)"
}

# 🎙️ BANCO DE DADOS DE SOTAQUES (FOCO EM PERNAMBUCO/ARCOVERDE)
banco_sotaques = {
    "pernambuco": {
        "alerta_comida": "🤖 Dudu: \"Oxente, {apelido}! Comida de fora de novo, visse?! A geladeira cheia de coisa e tu gastando com iFood... Desce desse carrinho, senão teu dinheiro vai mofar! 🙄\"",
        "alerta_roupa": "🤖 Dudu: \"Eita piula, {apelido}! Outro calçado ou blusa? Tu só tem dois pés e um corpo, rapaz. Vai deixar o armário entupido de pano! 👟\"",
        "segredo_confirmado": "🤖 Dudu: \"Fique tranquilo, {apelido}. O que tu me contar aqui morre aqui. Já apaguei da minha memória virtual, ninguém vai saber! 🔒🤫\"",
        "resposta_geral": "🤖 Dudu: \"Gasto anotado, {apelido}. Não sendo fuloragem desnecessária, eu apoio. 👀\""
    }
}

# 📱 FUNÇÃO DO BALÃO DE NOTIFICAÇÃO INTERATIVA E CHAT SEGURO
def receber_mensagem_app(mensagem_usuario, nivel_bateria=100):
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
        del segredo_temporario 
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

def solicitar_autenticacao():
    print("🔒 [Segurança]: O App do Dudu detectou uma tentativa de acesso.")
    if usuario["biometria_ativada"]:
        print("📸 [Face ID / Touch ID]: Escaneando rosto ou digital...")
        time.sleep(1) 
        usuario["celular_bloqueado"] = False
        print("🔓 [Acesso Permitido]: Identidade confirmada via biometria!")
        return True
    return False

# --- SIMULANDO O SEU APLICATIVO ---
print("📱 --- SEU APLICATIVO COM PRIVACIDADE E SEGURANÇA MÁXIMA --- \n")

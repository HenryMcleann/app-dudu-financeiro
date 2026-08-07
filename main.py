
import random
import time
import base64  # Biblioteca nativa para simular a criptografia oculta

# 🔒 MEMÓRIA CRIPTOGRAFADA, CARTEIRA E PREFERÊNCIAS DO HENRIQUE
usuario = {
    "nome": "Henrique",
    "apelido": "Henrique",
    "saldo_bancario": 1000.00,       
    "contador_ifood_seguido": 0,     
    "biometria_ativada": True,      
    "celular_bloqueado": True,      
    "contato_emergencia": "192 (SAMU)",
    "gps_localizacao_real": "pernambuco",   
    "modo_sotaque": "manual", 
    "sotaque_manual_escolhido": "pernambuco",
    
    # 🧠 BANCO DE DADOS OCULTO (Guarda as memórias em código para ninguém ler)
    "banco_memorias_criptografado": []
}

# 🎙️ DICIONÁRIO DE SOTAQUES REGIONAIS INTEGRADO
banco_sotaques = {
    "pernambuco": {
        "alerta_comida_normal": "🤖 Dudu: \"Oxente, {apelido}! Comida de fora de novo, visse?! Gastou R$ {valor:.2f}. A geladeira cheia de coisa... Desce desse carrinho! 🙄 Saldo atual: R$ {saldo:.2f}\"",
        "puxao_de_orelha_pesado": "🤖 Dudu: \"🚨 CHEGA, {apelido}! TRÊS VEZES SEGUIDAS gastando com delivery?! Tu tá achando que é sócio do iFood ou que dinheiro dá em árvore? Cansei! Saldo mofando em R$ {saldo:.2f}. Não falo mais nada! 🤬\"",
        "alerta_roupa": "🤖 Dudu: \"Eita piula, {apelido}! Gastou R$ {valor:.2f} com roupa? Tu só tem dois pés e um corpo, rapaz. Teu saldo foi para R$ {saldo:.2f} 👟\"",
        "segredo_confirmado": "🤖 Dudu: \"Fique tranquilo, {apelido}. O que tu me contar aqui some da tela na hora, visse?! Mas guardei o sentimento na minha memória blindada para te apoiar depois! 🔒🤫\"",
        "resposta_geral": "🤖 Dudu: \"Gasto de R$ {valor:.2f} anotado, {apelido}. Sobrou R$ {saldo:.2f}. 👀\""
    }
}

# 🔐 SISTEMA DE AUTENTICAÇÃO BIOMÉTRICA (NATIVA)
def solicitar_autenticacao():
    print("🔒 [Segurança]: O App do Dudu detectou uma tentativa de acesso.")
    if usuario["biometria_ativada"]:
        print("📸 [Face ID / Touch ID]: Escaneando rosto ou digital do Henrique...")
        time.sleep(1) 
        usuario["celular_bloqueado"] = False
        print("🔓 [Acesso Permitido]: Identidade confirmada com sucesso!")
        return True
    return False

# 🧠 FUNÇÃO DE ENGENHARIA DE MEMÓRIA CRIPTOGRAFADA
def salvar_memoria_oculta(mensagem_texto):
    # Transforma o texto normal em uma string codificada em base64 (Criptografia simples)
    mensagem_em_bytes = mensagem_texto.encode('utf-8')
    criptografado = base64.b64encode(mensagem_em_bytes).decode('utf-8')
    
    # Salva na gaveta oculta do aplicativo
    usuario["banco_memorias_criptografado"].append(criptografado)

def carregar_memorias_ocultas():
    print("\n🔍 [Área do Desenvolvedor]: Vasculhando o Banco de Dados oculto...")
    if not usuario["banco_memorias_criptografado"]:
        print("Nenhuma memória encontrada.")
        return
        
    for index, codificado in enumerate(usuario["banco_memorias_criptografado"]):
        # Descriptografa o texto para a IA ler de volta
        decodificado = base64.b64decode(codificado.encode('utf-8')).decode('utf-8')
        print(f" -> Registro {index+1} Criptografado no celular: {codificado} | Texto lido pela IA: \"{decodificado}\"")

# 📱 PROCESSADOR CENTRAL DO BALÃO DE NOTIFICAÇÃO E REGRAS DE NEGÓCIO
def receber_mensagem_app(mensagem_usuario, valor_movimentado=0.0, nivel_bateria=100):
    if usuario["celular_bloqueado"]:
        print("🚨 [Alerta]: O chat está trancado! Alguém pode estar tentando bisbilhotar.")
        if not solicitar_autenticacao():
            print("🔕 [Sistema]: Acesso bloqueado para proteger sua privacidade.")
            return
            
    msg = mensagem_usuario.lower()
    apelido = usuario["apelido"]
    regiao_ativa = usuario["sotaque_manual_escolhido"]
    sotaque = banco_sotaques[regiao_ativa]
    
    print("-" * 65)
    print(f"💬 [Balão] {apelido} disse: \"{mensagem_usuario}\"")
    
    # 🔒 GATILHO: MODO SEGREDO AUTODESTRUTIVO COM SALVAMENTO OCULTO
    if "segredo" in msg or "esconde" in msg:
        # Passo 1: Salva o segredo de forma oculta e criptografada na memória de longo prazo
        salvar_memoria_oculta(mensagem_usuario)
        
        # Passo 2: O Dudu responde usando o sotaque selecionado
        print(sotaque['segredo_confirmado'].format(apelido=apelido))
        
        # Passo 3: Destrói a mensagem visível na tela e na memória RAM instantaneamente
        del mensagem_usuario
        print("✨ [Sistema]: Texto apagado da tela e destruído. Salvo apenas no cofre criptografado da IA.")
        return

    # --- PROCESSAMENTO MATEMÁTICO NORMAL DE GASTOS ---
    usuario["saldo_bancario"] -= valor_movimentado
    saldo_limpo = usuario["saldo_bancario"]

    if "ifood" in msg or "delivery" in msg or "lanche" in msg:
        usuario["contador_ifood_seguido"] += 1
        if usuario["contador_ifood_seguido"] >= 3:
            print(sotaque["puxao_de_orelha_pesado"].format(apelido=apelido, saldo=saldo_limpo))
        else:
            print(sotaque["alerta_comida_normal"].format(apelido=apelido, valor=valor_movimentado, saldo=saldo_limpo))
    else:
        usuario["contador_ifood_seguido"] = 0
        print(sotaque["resposta_geral"].format(apelido=apelido, valor=valor_movimentado, saldo=saldo_limpo))

# ==============================================================================
# --- SIMULADOR EM AÇÃO NO GOOGLE COLAB ---
# ==============================================================================
print("📱 --- APP DUDU COM MEMÓRIA CRIPTOGRAFADA E AUTODESTRUIÇÃO --- \n")

# Passo 1: Abre o app via biometria
receber_mensagem_app("Gastei no iFood", valor_movimentado=40.00)

print("\n" + "="*70 + "\n")

# Passo 2: Henrique conta um segredo ultra pessoal. O texto some da tela na mesma hora!
receber_mensagem_app("Dudu, vou te contar um segredo: estou estudando programação escondido para mudar de vida")

print("\n" + "="*70 + "\n")

# Passo 3: Vamos testar o cérebro da IA para provar que o dado está guardado e protegido no cofre
carregar_memorias_ocultas()

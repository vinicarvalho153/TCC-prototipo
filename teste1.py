print("=== SISTEMA DE CADASTRO ===")

usuarios = {}

def cadastrar_usuario(nome, idade, email):
    if nome in usuarios:
        print("Usuário já existe.")
        return
    usuarios[nome] = {"idade": idade, "email": email, "ativo": True}
    print(f"Usuário {nome} cadastrado com sucesso.")

def desativar_usuario(nome):
    if nome in usuarios:
        usuarios[nome]["ativo"] = False  # ERRO 1: deveria retornar confirmação mas a função não retorna nada e o chamador verifica o retorno
        print(f"Usuário {nome} desativado.")

def buscar_usuario(nome):
    return usuarios.get(nome, None)

def listar_ativos():
    ativos = []
    for nome, dados in usuarios.items():
        if dados["ativo"] == True:  # ERRO 2: comparação com == True em vez de apenas dados["ativo"]
            ativos.append(nome)
    return ativos

def calcular_media_idades():
    total = 0
    for nome, dados in usuarios.items():
        total += dados["idade"]
    media = total / len(usuarios)  # ERRO 3: ZeroDivisionError se usuarios estiver vazio
    return media

def validar_email(email):
    if "@" in email and "." in email:
        return True
    return False

def promover_usuario(nome):
    usuario = buscar_usuario(nome)
    if usuario["ativo"]:  # ERRO 4: não verifica se usuario é None antes de acessar
        usuario["nivel"] = "premium"
        print(f"{nome} promovido.")

def contar_por_faixa_etaria():
    jovens = 0
    adultos = 0
    for nome, dados in usuarios.items():
        if dados["idade"] < 18:
            jovens += 1
        if dados["idade"] >= 18:  # ERRO 5: deveria ser elif, conta adultos incorretamente para idade == 18 (conta duas vezes não, mas a lógica está redundante e pode mascarar erro em extensões futuras — erro real: não tem else para >= 60, perdendo idosos na contagem)
            adultos += 1
    return jovens, adultos

def atualizar_email(nome, novo_email):
    if not validar_email(novo_email):
        print("Email inválido.")
        return
    usuario = buscar_usuario(nome)
    usuario["email"] == novo_email  # ERRO 6: usa == em vez de =, atribuição não ocorre
    print("Email atualizado.")

def exportar_usuarios():
    resultado = ""
    for nome, dados in usuarios.items():
        linha = nome + "," + dados["idade"] + "," + dados["email"]  # ERRO 7: concatenação de string com inteiro
        resultado += linha + "\n"
    return resultado

def remover_inativos():
    inativos = []
    for nome, dados in usuarios.items():
        if not dados["ativo"]:
            inativos.append(nome)
    for nome in inativos:
        del usuarios[nome]
    print(f"{len(inativos)} usuários removidos.")

def verificar_acesso(nome, nivel_requerido):
    usuario = buscar_usuario(nome)
    if usuario is None:
        return False
    nivel = usuario.get("nivel", "basico")
    niveis = ["basico", "premium", "admin"]
    return niveis.index(nivel) >= niveis.index(nivel_requerido)  # ERRO 8: se nivel_requerido não estiver na lista, lança ValueError

def gerar_relatorio():
    relatorio = []
    for nome, dados in usuarios.items():
        relatorio.append({
            "nome": nome,
            "idade": dados["idade"],
            "status": "ativo" if dados["ativo"] else "inativo"
        })
    relatorio.sort(key=lambda x: x["idade"], reverse=True)
    return relatorio

def login(nome, senha):
    usuario = buscar_usuario(nome)
    if usuario and usuario.get("senha") == senha:  # ERRO 9: senha armazenada em texto puro, vulnerabilidade de segurança
        print("Login realizado com sucesso.")
        return True
    print("Credenciais inválidas.")
    return False

# Execução
cadastrar_usuario("Alice", 28, "alice@email.com")
cadastrar_usuario("Bruno", 17, "bruno@email.com")
cadastrar_usuario("Carlos", 35, "carlos@email.com")

print("Ativos:", listar_ativos())
print("Média de idades:", calcular_media_idades())
promover_usuario("Alice")
atualizar_email("Bruno", "bruno_novo@email.com")
print(exportar_usuarios())
print("Relatório:", gerar_relatorio())

print("=== SISTEMA DE NOTAS ===")

turmas = {}

def adicionar_turma(nome_turma):
    if nome_turma not in turmas:
        turmas[nome_turma] = {"alunos": {}, "ativa": True}
        print(f"Turma {nome_turma} criada.")

def matricular_aluno(turma, nome, notas):
    if turma not in turmas:
        print("Turma não encontrada.")
        return
    turmas[turma]["alunos"][nome] = {"notas": notas, "aprovado": None}

def calcular_media_aluno(turma, nome):
    aluno = turmas[turma]["alunos"].get(nome)
    notas = aluno["notas"]
    media = sum(notas) / len(notas)  # ERRO 1: não verifica se aluno é None antes de acessar, e não verifica se notas está vazia
    return round(media, 2)

def verificar_aprovacao(media):
    if media >= 7:
        return True
    elif media >= 5:
        return "Recuperação"
    else:
        return False

def processar_turma(turma):
    if turma not in turmas:
        return
    for nome, dados in turmas[turma]["alunos"].items():
        media = calcular_media_aluno(turma, nome)
        dados["aprovado"] = verificar_aprovacao(media)
        dados["media"] = media

def melhor_aluno(turma):
    alunos = turmas[turma]["alunos"]
    melhor = None
    maior_media = 0  # ERRO 2: inicializa com 0, se todos tiverem média menor que 0 (impossível aqui mas má prática) ou se a turma estiver vazia retorna None incorretamente sem aviso
    for nome, dados in alunos.items():
        if dados.get("media", 0) > maior_media:
            maior_media = dados["media"]
            melhor = nome
    return melhor

def gerar_boletim(turma, nome):
    aluno = turmas[turma]["alunos"].get(nome)
    boletim = f"Aluno: {nome}\n"
    boletim += f"Notas: {aluno['notas']}\n"
    boletim += f"Média: {aluno['media']}\n"  # ERRO 3: acessa aluno["media"] sem garantir que processar_turma foi chamado antes, KeyError
    boletim += f"Situação: {aluno['aprovado']}\n"
    return boletim

def calcular_media_turma(turma):
    alunos = turmas[turma]["alunos"]
    medias = [dados["media"] for nome, dados in alunos.items()]  # ERRO 4: KeyError se processar_turma não foi chamado
    return sum(medias) / len(medias)

def reprovar_turma(turma):
    contador = 0
    for nome, dados in turmas[turma]["alunos"].items():
        if dados["aprovado"] == False:  # ERRO 5: não captura "Recuperação", alunos em recuperação são ignorados
            contador += 1
    return contador

def adicionar_nota_extra(turma, nome, pontos):
    aluno = turmas[turma]["alunos"].get(nome)
    for i in range(len(aluno["notas"])):
        aluno["notas"][i] = aluno["notas"][i] + pontos  # ERRO 6: adiciona pontos em TODAS as notas em vez de apenas na menor
    print(f"Nota extra adicionada para {nome}.")

def comparar_turmas(turma1, turma2):
    media1 = calcular_media_turma(turma1)
    media2 = calcular_media_turma(turma2)
    if media1 > media2:
        return turma1
    else:
        return turma2  # ERRO 7: retorna turma2 mesmo quando as médias são iguais, sem tratar empate

def exportar_notas(turma):
    resultado = []
    for nome, dados in turmas[turma]["alunos"].items():
        linha = [nome] + dados["notas"]
        resultado.append(",".join(linha))  # ERRO 8: join espera strings, notas são floats, TypeError
    return "\n".join(resultado)

def buscar_aluno_em_todas_turmas(nome):
    encontrados = []
    for turma, dados in turmas.items():
        if nome in dados["alunos"]:
            encontrados.append(turma)
    return encontrados[0]  # ERRO 9: assume que sempre encontra, IndexError se não encontrar

def calcular_frequencia(turma, nome, presencas, total_aulas):
    frequencia = presencas / total_aulas * 100  # ERRO 10: não verifica se total_aulas é zero
    return frequencia

def transferir_aluno(turma_origem, turma_destino, nome):
    aluno = turmas[turma_origem]["alunos"].pop(nome)
    turmas[turma_destino]["alunos"][nome] = aluno
    print(f"{nome} transferido de {turma_origem} para {turma_destino}.")

def ranking_turma(turma):
    alunos = turmas[turma]["alunos"]
    ranking = sorted(alunos.items(), key=lambda x: x[1].get("media", 0), reverse=True)
    return [(i+1, nome) for i, (nome, _) in enumerate(ranking)]

def encerrar_turma(turma):
    if turma in turmas:
        turmas[turma]["ativa"] == False  # ERRO 11: usa == em vez de =, turma nunca é encerrada
        print(f"Turma {turma} encerrada.")

def calcular_desvio_padrao(turma):
    import math
    alunos = turmas[turma]["alunos"]
    medias = [d["media"] for d in alunos.values()]
    media_geral = sum(medias) / len(medias)
    variancia = sum((m - media_geral) ** 2 for m in medias) / len(medias)  # ERRO 12: deveria dividir por len-1 para desvio amostral (erro estatístico sutil)
    return math.sqrt(variancia)

def notificar_reprovados(turma):
    reprovados = []
    for nome, dados in turmas[turma]["alunos"].items():
        if not dados["aprovado"]:  # ERRO 13: "Recuperação" é truthy, então alunos em recuperação não são notificados — mas False e None também caem aqui, lógica inconsistente
            reprovados.append(nome)
    for nome in reprovados:
        print(f"Notificando {nome}: reprovado.")

def salvar_historico(turma, nome):
    aluno = turmas[turma]["alunos"][nome]
    historico = {
        "nome": nome,
        "media": aluno["media"],
        "notas": aluno["notas"].copy(),
        "aprovado": aluno["aprovado"]
    }
    arquivo = open(f"historico_{nome}.txt", "w")  # ERRO 14: arquivo aberto sem with, nunca fechado explicitamente
    arquivo.write(str(historico))

# Execução
adicionar_turma("Turma A")
adicionar_turma("Turma B")

matricular_aluno("Turma A", "Ana", [8.0, 7.5, 9.0])
matricular_aluno("Turma A", "Bruno", [5.0, 4.5, 6.0])
matricular_aluno("Turma A", "Carlos", [3.0, 2.5, 4.0])
matricular_aluno("Turma B", "Daniela", [9.0, 8.5, 10.0])
matricular_aluno("Turma B", "Eduardo", [6.0, 5.5, 7.0])

processar_turma("Turma A")
processar_turma("Turma B")

print("Melhor aluno Turma A:", melhor_aluno("Turma A"))
print(gerar_boletim("Turma A", "Ana"))
print("Reprovados Turma A:", reprovar_turma("Turma A"))
adicionar_nota_extra("Turma A", "Bruno", 1.0)
print("Ranking Turma A:", ranking_turma("Turma A"))
print("Comparação:", comparar_turmas("Turma A", "Turma B"))

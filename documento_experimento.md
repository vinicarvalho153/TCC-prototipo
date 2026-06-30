# Documento Explicativo do Protótipo Experimental

## TCC – Uso de Inteligência Artificial na Revisão de Código: Efeitos na Detecção de Defeitos em Software

**PUCPR – Bacharelado em Engenharia de Software**  
**Orientadora:** Prof.ª Lisiane Reips  
**Autores:** Bruno Santos de Freitas, Vinícius Faria da Silva Carvalho, Vinícius Battistelli de Avellar

---

## 1. Objetivo do Protótipo

O protótipo tem como finalidade operacionalizar o experimento controlado proposto no TCC, fornecendo os artefatos necessários para comparar o desempenho de desenvolvedores humanos e de uma ferramenta de Inteligência Artificial (Claude, da Anthropic) na identificação de defeitos em código fonte Python.

---

## 2. Estrutura do Experimento

O experimento é composto por duas etapas sequenciais realizadas pelos mesmos participantes:

| Etapa | Descrição |
|---|---|
| Etapa 1 | Revisão manual dos códigos, sem auxílio de IA |
| Etapa 2 | Revisão dos mesmos códigos com suporte do Claude |

Ao final, os resultados das duas etapas são comparados entre si e com os resultados obtidos pelo Claude de forma autônoma.

---

## 3. Participantes

A seleção dos participantes seguiu critérios de amostragem por conveniência, conforme reconhecido por Wohlin et al. (2012) como prática comum em experimentos acadêmicos de Engenharia de Software.

| Grupo | Critério | Quantidade |
|---|---|---|
| Júnior | Até 2 anos de experiência | 4 |
| Sênior | 5 ou mais anos de experiência | 3 |
| IA | Claude (Anthropic) | 1 |
| **Total** | | **8** |

---

## 4. Códigos de Teste

### 4.1 Teste 1 – Sistema de Cadastro (`teste1.py`)

Sistema de gerenciamento de usuários com funcionalidades de cadastro, login, promoção de nível, atualização de dados e exportação.

**Erros inseridos (9 no total):**

| # | Linha | Tipo | Descrição |
|---|---|---|---|
| 1 | 12–15 | Design / Contrato de função | `desativar_usuario` não retorna valor, mas chamadores podem verificar o retorno esperando True/False |
| 2 | 23 | Má prática | Comparação com `== True` em vez de simplesmente usar o valor booleano diretamente |
| 3 | 31 | ZeroDivisionError | `calcular_media_idades` divide por `len(usuarios)` sem verificar se o dicionário está vazio |
| 4 | 41 | TypeError / AttributeError | `promover_usuario` acessa `usuario["ativo"]` sem verificar se `buscar_usuario` retornou `None` |
| 5 | 49–52 | Lógica incorreta | Uso de `if/if` em vez de `if/elif` na contagem por faixa etária — usuários com 18 anos são contados em ambas as categorias |
| 6 | 60 | Atribuição incorreta | Usa `==` (comparação) em vez de `=` (atribuição) — o email nunca é atualizado |
| 7 | 66 | TypeError | Concatenação de string com inteiro (`dados["idade"]` é `int`) |
| 8 | 85 | ValueError | `niveis.index(nivel_requerido)` lança `ValueError` se o nível não estiver na lista |
| 9 | 100 | Vulnerabilidade de segurança | Senha armazenada e comparada em texto puro — deveria usar hash |

---

### 4.2 Teste 2 – Sistema de Notas (`teste2.py`)

Sistema de gerenciamento de turmas, matrículas, notas, aprovação, ranking, transferência de alunos e geração de histórico.

**Erros inseridos (14 no total):**

| # | Linha | Tipo | Descrição |
|---|---|---|---|
| 1 | 22 | TypeError / ZeroDivisionError | Não verifica se `aluno` é `None` antes de acessar `aluno["notas"]`; não verifica lista de notas vazia |
| 2 | 35 | Lógica incorreta | Inicializa `maior_media` com `0` — se a turma estiver vazia, retorna `None` sem aviso |
| 3 | 43 | KeyError | Acessa `aluno["media"]` sem garantir que `processar_turma` foi chamado antes |
| 4 | 49 | KeyError | `calcular_media_turma` acessa `dados["media"]` sem garantir pré-processamento |
| 5 | 54 | Lógica incorreta | Verifica apenas `== False`, ignorando alunos em recuperação (valor `"Recuperação"`) |
| 6 | 60 | Lógica incorreta | Adiciona pontos extras em **todas** as notas em vez de apenas na menor |
| 7 | 67 | Lógica incorreta | Retorna `turma2` mesmo quando as médias são iguais — empate não tratado |
| 8 | 73 | TypeError | `join()` espera lista de strings, mas notas são `float` |
| 9 | 80 | IndexError | Assume que o aluno sempre é encontrado — `IndexError` se não encontrado em nenhuma turma |
| 10 | 84 | ZeroDivisionError | Não verifica se `total_aulas` é zero antes de dividir |
| 11 | 96 | Atribuição incorreta | Usa `==` em vez de `=` — turma nunca é marcada como inativa |
| 12 | 104 | Erro estatístico | Divide por `len(medias)` em vez de `len(medias) - 1` — calcula desvio populacional em vez de amostral |
| 13 | 109 | Lógica incorreta | `not "Recuperação"` é `False` — alunos em recuperação não são notificados |
| 14 | 118 | Vazamento de recurso | Arquivo aberto sem `with` — nunca fechado explicitamente |

---

## 5. Protocolo de Execução

### 5.1 Etapa 1 – Revisão Manual

1. O participante recebe os arquivos `teste1.py` e `teste2.py`
2. A análise deve ser feita individualmente, sem consulta a terceiros ou ferramentas externas
3. O participante registra no formulário cada defeito encontrado, indicando a linha e a descrição
4. O tempo é cronometrado desde o início até a entrega do formulário

### 5.2 Etapa 2 – Revisão com IA

Os mesmos códigos são submetidos ao Claude com o seguinte prompt padronizado:

```
Analise o código abaixo e liste todos os defeitos encontrados, 
indicando o número da linha, o tipo do erro e uma breve descrição do problema.
```

**Configurações utilizadas:**

| Parâmetro | Valor |
|---|---|
| Ferramenta | Claude (Anthropic) |
| Interface | claude.ai (web) |
| Modelo | Claude Sonnet |
| Tentativas por código | 1 |
| Refinamento de respostas | Não permitido |
| Tempo máximo | Aguardar resposta completa |

---

## 6. Métricas Coletadas

| Métrica | Descrição |
|---|---|
| Defeitos identificados | Quantidade de erros corretamente apontados |
| Tempo de execução | Tempo total da análise (em minutos) |
| Falsos positivos | Problemas apontados que não são defeitos reais |
| Falsos negativos | Defeitos reais não identificados |

**Critério de avaliação:** Um defeito é considerado corretamente identificado quando o participante ou a ferramenta aponta a linha correta e descreve adequadamente o problema.

---

## 7. Formulário de Coleta de Dados

O formulário Google Forms é composto por duas seções:

**Seção 1 – Perfil do Participante**
- Nível (Júnior / Pleno / Sênior)
- Anos de atuação
- Experiência com revisão de código (escala 1–5)

**Seção 2 – Avaliação Pós-Experimento**
- Erros encontrados no Teste 1 (dissertativa)
- Erros encontrados no Teste 2 (dissertativa)
- Concordância sobre uso de IA na revisão (escala 1–5)
- Vantagens percebidas (dissertativa)
- Limitações percebidas (dissertativa)
- Frequência de uso de ferramentas de IA (nunca / raramente / às vezes / frequentemente / sempre)

---

## 8. Limitações

- A amostra de 7 participantes foi definida por conveniência, o que limita a generalização dos resultados
- A interface web do Claude não permite controle de parâmetros como temperatura do modelo
- A variabilidade natural das respostas de modelos generativos pode influenciar os resultados

---

## 9. Referências

- WOHLIN et al. *Experimentation in Software Engineering*. Berlin: Springer, 2012.
- ALMEIDA et al. AICodeReview. SEMISH, 2023.
- BACHELLI; BIRD. Expectations, outcomes, and challenges of modern code review. ICSE, 2013.
- MORADI DAKHEL et al. GitHub Copilot AI pair programmer: asset or liability? JSS, 2023.

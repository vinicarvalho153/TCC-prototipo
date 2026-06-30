# TCC – Uso de Inteligência Artificial na Revisão de Código

## Efeitos na Detecção de Defeitos em Software

**Pontifícia Universidade Católica do Paraná – PUCPR**  
Bacharelado em Engenharia de Software  
Orientadora: Prof.ª Lisiane Reips  

**Autores:**
- Bruno Santos de Freitas
- Vinícius Faria da Silva Carvalho
- Vinícius Battistelli de Avellar

---

## Sobre o Projeto

Este repositório contém o protótipo experimental desenvolvido para o Trabalho de Conclusão de Curso (TCC), cujo objetivo é comparar o desempenho de desenvolvedores humanos e ferramentas de Inteligência Artificial na identificação de defeitos em código fonte.

O experimento consiste na análise de dois códigos Python com defeitos propositalmente inseridos, realizados por dois grupos de desenvolvedores (júnior e sênior) e pela ferramenta de IA Claude (Anthropic). Os resultados são comparados por meio de métricas quantitativas: número de defeitos encontrados, tempo de execução e taxas de falsos positivos e negativos.

---

## Estrutura do Repositório

```
TCC-prototipo/
│
├── teste1.py              # Código 1 – Sistema de Cadastro (9 erros de sintaxe e design)
├── teste2.py              # Código 2 – Sistema de Notas (14 erros de lógica e runtime)
├── gabarito.txt           # Gabarito completo com descrição de todos os erros
├── documento_experimento.md  # Documentação detalhada do experimento
└── README.md              # Este arquivo
```

---

## Códigos de Teste

### teste1.py – Sistema de Cadastro
- **Linguagem:** Python 3
- **Tema:** Sistema de gerenciamento de usuários com cadastro, login, promoção e exportação
- **Quantidade de erros inseridos:** 9
- **Tipo de erros:** erros de design, má prática, vulnerabilidade de segurança, TypeError, ZeroDivisionError, atribuição incorreta com `==`, acesso a `None` sem verificação

### teste2.py – Sistema de Notas
- **Linguagem:** Python 3
- **Tema:** Sistema de gerenciamento de turmas, alunos e notas com aprovação, ranking e relatórios
- **Quantidade de erros inseridos:** 14
- **Tipo de erros:** KeyError por dependência de ordem, lógica incorreta de contagem, TypeError em join, ZeroDivisionError, IndexError, erro estatístico no desvio padrão, arquivo não fechado, atribuição incorreta com `==`

---

## Como Executar

### Requisitos
- Python 3.8 ou superior

### Execução
```bash
# Clonar o repositório
git clone https://github.com/vinicarvalho153/TCC-prototipo.git
cd TCC-prototipo

# Executar os códigos de teste
python teste1.py
python teste2.py
```

> **Atenção:** Os códigos contêm erros propositais. Alguns erros causam exceções em tempo de execução. O objetivo é que os participantes identifiquem os problemas por meio de leitura e análise estática do código, não apenas pela execução.

---

## Protocolo do Experimento

### Participantes
- 4 desenvolvedores júnior (até 2 anos de experiência)
- 3 desenvolvedores sênior (5 ou mais anos de experiência)
- 1 ferramenta de IA: **Claude (Anthropic)** – modelo Claude Sonnet

### Etapas
1. **Revisão manual** – participantes analisam os códigos sem auxílio de IA
2. **Revisão com IA** – os mesmos códigos são submetidos ao Claude com prompt padronizado

### Prompt Utilizado com a IA
```
Analise o código abaixo e liste todos os defeitos encontrados, 
indicando o número da linha, o tipo do erro e uma breve descrição do problema.
```

### Configurações da IA
| Parâmetro | Valor |
|---|---|
| Ferramenta | Claude (Anthropic) |
| Interface | claude.ai (web) |
| Tentativas por código | 1 (única interação) |
| Refinamento de respostas | Não permitido |
| Tempo máximo | Aguardar resposta completa |

### Métricas Coletadas
- Número de defeitos identificados
- Tempo de execução da análise
- Taxa de falsos positivos
- Taxa de falsos negativos

---

## Gabarito

O arquivo `gabarito.txt` contém a lista completa de todos os erros inseridos em cada código, com número de linha, tipo do erro e descrição. Este arquivo é utilizado como referência para avaliar os resultados dos participantes e da IA.

---

## Formulário de Coleta de Dados

Os participantes respondem um formulário Google Forms com:
- Perfil (nível, anos de experiência, formação)
- Erros encontrados no Teste 1
- Erros encontrados no Teste 2
- Avaliação sobre o uso de IA na revisão de código

---

## Referências

- WOHLIN et al. *Experimentation in Software Engineering*. Berlin: Springer, 2012.
- ALMEIDA et al. AICodeReview. SEMISH, 2023.
- BACHELLI; BIRD. Expectations, outcomes, and challenges of modern code review. ICSE, 2013.

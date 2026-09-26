# Resolução de Equações Não Lineares — Métodos Numéricos

APS (Avaliação Prática Supervisionada) da disciplina de **Métodos Numéricos Computacionais** — Ciência da Computação.

Implementação e comparação de três métodos iterativos clássicos para encontrar raízes de equações não lineares, aplicados à função:

```
f(x) = x³ − 2x − 5
```

## Métodos implementados

| Método | Estratégia | Estimativa(s) inicial(is) |
|---|---|---|
| **Bisseção** | Divide o intervalo ao meio, mantendo o subintervalo com troca de sinal (Teorema de Bolzano) | `[a, b] = [2, 3]` |
| **Newton-Raphson** | Usa a reta tangente (derivada analítica exata `f'(x) = 3x² − 2`) | `x₀ = 2` |
| **Secantes** | Aproxima a derivada por diferenças finitas entre dois pontos | `x₀ = 2`, `x₁ = 3` |

Todos os métodos usam tolerância `ε = 10⁻⁶` e limite máximo de `100` iterações, parando quando `|x_{k+1} − x_k| < ε` ou `|f(x_k)| < ε`.

## Resultados

Raiz de referência: `x* ≈ 2,0945514815`

| Método | Iterações | Raiz encontrada | Erro absoluto | Erro relativo (%) |
|---|---|---|---|---|
| Bisseção | 20 | 2,0945520401 | 5,59 × 10⁻⁷ | 0,000027% |
| Newton-Raphson | 3 | 2,0945514817 | 1,98 × 10⁻¹⁰ | 0,00000001% |
| Secantes | 5 | 2,0945514812 | 2,72 × 10⁻¹⁰ | 0,00000001% |

**Conclusão:** Newton-Raphson converge mais rápido (ordem quadrática), Secantes é uma boa alternativa quando a derivada analítica não está disponível (ordem superlinear, ~1,618), e Bisseção é o mais lento porém o mais robusto (convergência linear garantida).

## Como executar

Requer apenas Python 3 (não há dependências externas).

```bash
python3 metodos_numericos.py
```

Saída esperada:

```
Metodo          Iteracoes   Raiz                Erro Abs.       Erro Rel. (%)   Tempo (s)
------------------------------------------------------------------------------------------------
Bisseccao       20          2.0945520401        5.59e-07        0.000027        0.000062
Newton-Raphson  3           2.0945514817        1.98e-10        0.000000        0.000011
Secantes        5           2.0945514812        2.72e-10        0.000000        0.000017
```

## Estrutura

```
.
├── metodos_numericos.py   # Implementação dos três métodos
└── README.md
```

## Autor

Caio Ferreira da Silva — Matrícula 2023100040

"""
Metodos Numericos para Resolucao de Equacoes Nao Lineares
APS - Metodos Numericos Computacionais

Funcao de estudo: f(x) = x^3 - 2x - 5
Derivada: f'(x) = 3x^2 - 2
Raiz de referencia: x* ~= 2.0945514815

Implementa os metodos da Bisseccao, Newton-Raphson e das Secantes.
"""

import time

def f(x):
    """Funcao alvo: f(x) = x^3 - 2x - 5."""
    return x**3 - 2*x - 5


def df(x):
    """Derivada analitica de f: f'(x) = 3x^2 - 2."""
    return 3*x**2 - 2


X_REF = 2.0945514815
TOL = 1e-6
N_MAX = 100


def bissecao(f, a, b, tol=TOL, n_max=N_MAX):
    """Metodo da Bisseccao."""
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")

    historico = []
    x_ant = a
    for i in range(1, n_max + 1):
        xm = (a + b) / 2.0
        fxm = f(xm)
        historico.append((i, xm, fxm))

        if abs(xm - x_ant) < tol or abs(fxm) < tol:
            return xm, i, historico

        if f(a) * fxm < 0:
            b = xm
        else:
            a = xm
        x_ant = xm

    return xm, n_max, historico


def newton_raphson(f, df, x0, tol=TOL, n_max=N_MAX):
    """Metodo de Newton-Raphson."""
    x = x0
    historico = []
    for i in range(1, n_max + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivada nula durante a iteracao.")

        x_novo = x - fx / dfx
        historico.append((i, x_novo, f(x_novo)))

        if abs(x_novo - x) < tol or abs(f(x_novo)) < tol:
            return x_novo, i, historico

        x = x_novo

    return x, n_max, historico


def secantes(f, x0, x1, tol=TOL, n_max=N_MAX):
    """Metodo das Secantes."""
    historico = []
    for i in range(1, n_max + 1):
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            raise ZeroDivisionError("Divisao por zero (f(x1) - f(x0) = 0).")

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        historico.append((i, x2, f(x2)))

        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return x2, i, historico

        x0, x1 = x1, x2

    return x2, n_max, historico


def erro_absoluto(x_aprox, x_ref=X_REF):
    return abs(x_ref - x_aprox)


def erro_relativo_percentual(x_aprox, x_ref=X_REF):
    return abs(x_ref - x_aprox) / abs(x_ref) * 100.0


def main():
    resultados = {}

    t0 = time.perf_counter()
    raiz_b, it_b, hist_b = bissecao(f, 2.0, 3.0)
    t_b = time.perf_counter() - t0
    resultados["Bisseccao"] = (raiz_b, it_b, t_b)

    t0 = time.perf_counter()
    raiz_n, it_n, hist_n = newton_raphson(f, df, 2.0)
    t_n = time.perf_counter() - t0
    resultados["Newton-Raphson"] = (raiz_n, it_n, t_n)

    t0 = time.perf_counter()
    raiz_s, it_s, hist_s = secantes(f, 2.0, 3.0)
    t_s = time.perf_counter() - t0
    resultados["Secantes"] = (raiz_s, it_s, t_s)

    print(f"{'Metodo':<16}{'Iteracoes':<12}{'Raiz':<20}{'Erro Abs.':<16}{'Erro Rel. (%)':<16}{'Tempo (s)'}")
    print("-" * 96)
    for nome, (raiz, it, tempo) in resultados.items():
        eabs = erro_absoluto(raiz)
        erel = erro_relativo_percentual(raiz)
        print(f"{nome:<16}{it:<12}{raiz:<20.10f}{eabs:<16.2e}{erel:<16.6f}{tempo:.6f}")

    return resultados


if __name__ == "__main__":
    main()

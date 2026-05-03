def gerar_sequencia(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")

    seq = []
    a, b = 0, 1

    for _ in range(n):
        seq.append(a)
        a, b = b, a + b

    return seq


def termo(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


def recursivo(n):
    if n <= 1:
        return n
    return recursivo(n - 1) + recursivo(n - 2)
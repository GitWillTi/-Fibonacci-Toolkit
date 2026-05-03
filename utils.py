import json

def salvar_em_arquivo(nome, dados):
    with open(nome, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_arquivo(nome):
    try:
        with open(nome, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def mostrar_estatisticas(seq):
    if not seq:
        return "Sequência vazia"

    return {
        "tamanho": len(seq),
        "maior": max(seq),
        "menor": min(seq),
        "soma": sum(seq)
    }
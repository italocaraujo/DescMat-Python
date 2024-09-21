def desenhar_montanha(altura):
    """Desenha uma montanha usando o caractere #.

    Args:
        altura: A altura da montanha.
    """

    for i in range(altura):
        espacos = altura - i - 1
        hashes = 2 * i + 1
        print(" " * espacos + "#" * hashes)

# Exemplo de uso:
desenhar_montanha(5)
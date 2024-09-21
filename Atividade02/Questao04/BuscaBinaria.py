def busca_binaria(lista, elemento):
  """Realiza uma busca binária em uma lista ordenada.

  Args:
    lista: A lista ordenada onde será realizada a busca.
    elemento: O elemento a ser buscado.

  Returns:
    O índice do elemento, se encontrado, caso contrário, -1.
  """

  esquerda = 0
  direita = len(lista) - 1

  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    if lista[meio] == elemento:
      return meio
    elif lista[meio] < elemento:
      esquerda = meio + 1
    else:
      direita = meio - 1

  return -1
def busca_linear(lista, elemento):
  """Realiza uma busca linear em uma lista.

  Args:
    lista: A lista onde será realizada a busca.
    elemento: O elemento a ser buscado.

  Returns:
    O índice do elemento, se encontrado, caso contrário, -1.
  """

  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return -1


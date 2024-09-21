def somatorio(f, n, a):
  """Calcula o somatório de f(a) + f(a+1) + ... + f(a+n).

  Args:
    f: Função a ser aplicada em cada termo da soma.
    n: Número de termos da soma.
    a: Valor inicial.

  Returns:
    A soma dos valores calculados pela função f.
  """

  soma = 0
  for i in range(n+1):
    soma += f(a+i)
  return soma

def quadrado(x):
  return x**2

resultado = somatorio(quadrado, 3, 2)  # Calcula 2^2 + 3^2 + 4^2
print(resultado)

def somatorio(f, n, a, g=None):
  """Calcula o somatório de f(a) + f(a+1) + ... + f(a+n) ou
  g(f(a)) + g(f(a+1)) + ... + g(f(a+n)) se g for fornecida.

  Args:
    f: Função a ser aplicada em cada termo da soma.
    n: Número de termos da soma.
    a: Valor inicial.
    g: Função opcional a ser aplicada após f.

  Returns:
    A soma dos valores calculados.
  """

  soma = 0
  for i in range(n+1):
    valor = f(a+i)
    if g:
      valor = g(valor)
    soma += valor
  return soma

def dobro(x):
  return 2*x

resultado = somatorio(quadrado, 3, 2, dobro)  # Calcula 2*2^2 + 2*3^2 + 2*4^2
print(resultado)
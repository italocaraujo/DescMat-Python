from math import gcd

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        """Simplifica a fração para a forma mais reduzida."""
        mdc = gcd(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc
        if self.denominador < 0:  # Mantém o denominador positivo
            self.numerador *= -1
            self.denominador *= -1

    def __add__(self, outra):
        """Soma duas frações."""
        numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        return Fracao(numerador, denominador)

    def __sub__(self, outra):
        """Subtrai duas frações."""
        numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        return Fracao(numerador, denominador)

    def __mul__(self, outra):
        """Multiplica duas frações."""
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        return Fracao(numerador, denominador)

    def __truediv__(self, outra):
        """Divide duas frações."""
        if outra.numerador == 0:
            raise ValueError("Não é possível dividir por uma fração de numerador zero.")
        numerador = self.numerador * outra.denominador
        denominador = self.denominador * outra.numerador
        return Fracao(numerador, denominador)

    def __eq__(self, outra):
        """Compara se duas frações são iguais."""
        return self.numerador * outra.denominador == self.denominador * outra.numerador

    def __lt__(self, outra):
        """Compara se a fração é menor que outra fração."""
        return self.numerador * outra.denominador < self.denominador * outra.numerador

    def __gt__(self, outra):
        """Compara se a fração é maior que outra fração."""
        return self.numerador * outra.denominador > self.denominador * outra.numerador

    def to_decimal(self):
        """Converte a fração para um número decimal."""
        return self.numerador / self.denominador

    def __str__(self):
        """Retorna a fração no formato 'numerador/denominador'."""
        return f"{self.numerador}/{self.denominador}"

# Testando a classe Fracao
f1 = Fracao(1, 2)
f2 = Fracao(3, 4)

# Operações
print(f"Adição: {f1} + {f2} = {f1 + f2}")
print(f"Subtração: {f1} - {f2} = {f1 - f2}")
print(f"Multiplicação: {f1} * {f2} = {f1 * f2}")
print(f"Divisão: {f1} / {f2} = {f1 / f2}")

# Comparações
print(f"Comparação de igualdade: {f1} == {f2}: {f1 == f2}")
print(f"{f1} é maior que {f2}? {f1 > f2}")
print(f"{f1} é menor que {f2}? {f1 < f2}")

# Conversão para decimal
print(f"{f1} em decimal é {f1.to_decimal()}")

# Fração simplificada
f3 = Fracao(6, 8)
print(f"A fração {f3} simplificada é {f3}")

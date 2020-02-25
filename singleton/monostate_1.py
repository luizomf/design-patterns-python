"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state: dict = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MonoStateSimple(nome='Luiz')
    m2 = MonoStateSimple(sobrenome='Miranda')
    print(m1)
    print(m2)

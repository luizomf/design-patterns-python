"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()  # Hook
        self.add_ingrentients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza.')

    @abstractmethod
    def add_ingrentients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    def add_ingrentients(self) -> None:
        print(f'AModa - adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None:
        print(f'AModa - cozinhado por 45min no forno a lenha')


class Veg(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Veg - Lavando ingredientes')

    def add_ingrentients(self) -> None:
        print(f'Veg - adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        print(f'Veg - cozinhado por 5min no forno comum')


if __name__ == "__main__":
    a_moda = AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()

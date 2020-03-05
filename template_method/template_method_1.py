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


class Abstract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self) -> None: pass

    def base_class_method(self) -> None:
        print('OLÁ EU SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM')

    @abstractmethod
    def operation1(self) -> None: pass

    @abstractmethod
    def operation2(self) -> None: pass


class ConcreteClass1(Abstract):
    def hook(self) -> None:
        print('Olha eu vou utilizar o hook')

    def operation1(self) -> None:
        print('Operaçao 1 concluída')

    def operation2(self) -> None:
        print('Operaçao 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self) -> None:
        print('Operaçao 1 concluída (de maneira diferente)')

    def operation2(self) -> None:
        print('Operaçao 2 concluída  (de maneira diferente)')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()

"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.

Observação importante: qualquer classe que se enquadrar na descrição acima e
que tenha um método que cria objetos, está no padrão Factory Method.
"""
from abc import ABC, abstractmethod

# =============================================================================
# Product
# =============================================================================


class Impressora(ABC):
    """Product"""
    @abstractmethod
    def imprimir(self): pass


# =============================================================================
# Concret Products
# =============================================================================


class ImpressoraMultifuncional(Impressora):
    """Concrete Product"""

    def imprimir(self):
        print('Impressora Multifuncional está imprimindo')


class ImpressoraSimples(Impressora):
    """Concrete Product"""

    def imprimir(self):
        print('Impressora Simples está imprimindo')


class ImpressoraAvancada(Impressora):
    """Concrete Product"""

    def imprimir(self):
        print('Impressora Avançada está imprimindo')


class OutraImpressora(Impressora):
    """Concrete Product"""

    def imprimir(self):
        print('Outra impressora está imprimindo')


# =============================================================================
# Creator
# =============================================================================

class ImpressoraCreator(ABC):
    """Creator"""
    @staticmethod
    @abstractmethod
    def criar(): pass


# =============================================================================
# Concrete Creators
# =============================================================================


class ImpressoraMultifuncionalCreator(ImpressoraCreator):
    """Concrete Creator"""
    @staticmethod
    def criar():
        """Factory Method"""
        return ImpressoraMultifuncional()


class ImpressoraSimplesCreator(ImpressoraCreator):
    """Concrete Creator"""
    @staticmethod
    def criar():
        """Factory Method"""
        return ImpressoraSimples()


class ImpressoraAvancadaCreator(ImpressoraCreator):
    """Concrete Creator"""
    @staticmethod
    def criar():
        """Factory Method"""
        return ImpressoraAvancada()


class OutraImpressoraCreator(ImpressoraCreator):
    """Concrete Creator"""
    @staticmethod
    def criar():
        """Factory Method"""
        return OutraImpressora()


if __name__ == "__main__":
    # =========================================================================
    # Código cliente
    # =========================================================================

    impressora_multifuncional = ImpressoraMultifuncionalCreator.criar()
    impressora_simples = ImpressoraSimplesCreator.criar()
    impressora_avancada = ImpressoraAvancadaCreator.criar()
    outra_impressora = OutraImpressoraCreator.criar()

    impressoras = [impressora_multifuncional,
                   impressora_simples, impressora_avancada, outra_impressora]

    for imp in impressoras:
        imp.imprimir()

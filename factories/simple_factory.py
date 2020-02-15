"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe, método ou
função que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

    Simple factory não é considerada padrão de projeto, mas geralmente livros
    trazem este projeto como uma base para o entendimento de Factory Method e
    Abstract factory.

Vamos ver 3 tipos de Factory: Simple factory (não GoF), Factory method e
Abstract Factory
"""
from abc import ABC, abstractmethod


class Impressora(ABC):
    @abstractmethod
    def imprimir(self): pass


class ImpressoraMultifuncional(Impressora):
    def imprimir(self):
        print('Impressora Multifuncional está imprimindo')


class ImpressoraSimples(Impressora):
    def imprimir(self):
        print('Impressora Simples está imprimindo')


class ImpressoraAvancada(Impressora):
    def imprimir(self):
        print('Impressora Avançada está imprimindo')


class ImpressoraFactory:
    @staticmethod
    def criar(tipo):
        if tipo == 'multifuncional':
            return ImpressoraMultifuncional()
        if tipo == 'simples':
            return ImpressoraSimples()
        if tipo == 'avancada':
            return ImpressoraAvancada()
        assert 0, 'Impressora não foi encontrada'


if __name__ == "__main__":
    impressora_multifuncional = ImpressoraFactory.criar('multifuncional')
    impressora_simples = ImpressoraFactory.criar('simples')
    impressora_avancada = ImpressoraFactory.criar('avancada')

    impressoras = [impressora_multifuncional,
                   impressora_simples, impressora_avancada]

    for imp in impressoras:
        imp.imprimir()

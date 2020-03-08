# O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
# É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR.

from __future__ import annotations
from enum import Enum, auto


class Payment(Enum):
    """
    Definimos um enum com as opções de estado
    que o nosso objeto Order pode ter
    """
    Pending = auto()
    Approved = auto()
    Rejected = auto()

    def __str__(self):
        """
        O retorno aqui será o nome da classe (Payment)
        mais o nome do membro. Ex.: PaymentApproved
        """
        return f'{self.__class__.__name__}{self.name}'


class Order:
    def __init__(self) -> None:
        self.state: Payment = Payment.Pending

    def change_state(self, state: Payment):
        """
        O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
        É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR.
        """

        # Pending
        if self.state == Payment.Pending and state == Payment.Pending:
            print('Pagamento já pendente, não vou mover para pendente.')
        elif self.state == Payment.Pending and state == Payment.Approved:
            self.state = Payment.Approved
            print('Pagamento aprovado')
        elif self.state == Payment.Pending and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Pagamento recusado')

        # Approved
        elif self.state == Payment.Approved and state == Payment.Approved:
            print('Pagamento já aprovado, não vou aprovar novamente.')
        elif self.state == Payment.Approved and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Pagamento Recusado')
        elif self.state == Payment.Approved and state == Payment.Pending:
            self.state = Payment.Pending
            print('Pagamento pendente')

        # Rejected
        elif self.state == Payment.Rejected and state == Payment.Approved:
            print('Pagamento recusado. Não posso aprovar')
        elif self.state == Payment.Rejected and state == Payment.Rejected:
            print('Pagamento recusado. Não posso recusar novamente')
        elif self.state == Payment.Rejected and state == Payment.Pending:
            print('Pagamento recusado. Não posso mover para pendente')

        print(f'Estado atual: {self.state}')
        print()

    def pending(self) -> None:
        print('Tentando executar pending(Payment.Pending)')
        self.change_state(Payment.Pending)

    def approve(self) -> None:
        print('Tentando executar approve(Payment.Approved)')
        self.change_state(Payment.Approved)

    def reject(self) -> None:
        print('Tentando executar reject(Payment.Rejected)')
        self.change_state(Payment.Rejected)


if __name__ == "__main__":
    o1 = Order()
    o1.approve()
    o1.approve()
    o1.reject()
    o1.approve()
    o1.pending()

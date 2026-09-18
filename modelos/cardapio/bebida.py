from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho, descricao):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome.ljust(25)} | {f"R${self._preco:.2f}".ljust(25)} | {self._tamanho.ljust(25)} | {self._descricao}'
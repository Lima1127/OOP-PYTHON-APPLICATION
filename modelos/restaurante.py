from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacao).ljust(25) if self.media_avaliacao != 0 else "Sem avaliações".ljust(25)} | {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def status(self):
        return 'Ativado✅' if self._status else 'Desativado❎'

    def alternar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, nota, cliente):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(nota, cliente)
            self._avaliacao.append(avaliacao)
        else:
            print('Nota inválida. A nota deve estar entre 0 e 5.')


    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma / len(self._avaliacao), 1)


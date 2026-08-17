class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def status(self):
        return 'Ativado✅' if self._status else 'Desativado❎'


restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Churrasco')

Restaurante.listar_restaurantes()




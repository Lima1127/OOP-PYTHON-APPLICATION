from modelos.restaurante import Restaurante

restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Hamburguer')
restaurante_outback = Restaurante('Outback', 'Australiano')

restaurante_sujinho.alternar_status()

restaurante_sujinho.receber_avaliacao(8, 'João')
restaurante_sujinho.receber_avaliacao(4, 'Maria')
restaurante_sujinho.receber_avaliacao(10, 'Pedro')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
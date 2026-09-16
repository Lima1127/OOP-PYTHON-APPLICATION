from modelos.restaurante import Restaurante

restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Hamburguer')
restaurante_outback = Restaurante('Outback', 'Australiano')

restaurante_sujinho.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
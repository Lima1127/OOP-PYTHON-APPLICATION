from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Hamburguer')
restaurante_outback = Restaurante('Outback', 'Australiano')

restaurante_sujinho.alternar_status()

bebida1 = Bebida('Coca-Cola', 5.0, 'grande', 'Refrigerante de cola')
prato1 = Prato('Hamburguer', 60.0, 'Hamburguer com queijo e bacon')

def main():
    print(bebida1)
    print(prato1)

if __name__ == '__main__':
    main()
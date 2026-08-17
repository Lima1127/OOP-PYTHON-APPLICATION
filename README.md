# 🍽️ Restaurante — Estudo de OOP em Python

Projeto desenvolvido durante meus estudos de **Programação Orientada a Objetos (OOP)** utilizando Python.

O objetivo deste projeto é praticar conceitos fundamentais de classes, objetos, atributos, métodos, métodos de classe e propriedades.

## 📚 Conceitos praticados

Neste projeto foram utilizados os seguintes conceitos:

* Classes
* Objetos e instâncias
* Construtor `__init__`
* Atributos de instância
* Atributos de classe
* Métodos de instância
* `@classmethod`
* `@property`
* Encapsulamento
* Método especial `__str__`
* Lista de objetos

## 🏗️ Estrutura da classe

A classe principal do projeto é `Restaurante`.

```python
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        Restaurante.restaurantes.append(self)
```

### Atributo de classe

```python
restaurantes = []
```

Essa lista pertence à **classe**, e não a uma instância específica.

Ela é utilizada para armazenar todos os objetos `Restaurante` criados.

Por exemplo:

```python
restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Churrasco')
```

Os dois objetos são adicionados automaticamente à lista:

```python
Restaurante.restaurantes
```

## 🔒 Encapsulamento

Os atributos foram definidos utilizando `_`:

```python
self._nome
self._categoria
self._status
```

O `_` indica que esses atributos são considerados **internos/protegidos**, sendo uma convenção utilizada em Python para indicar que eles não deveriam ser acessados diretamente de fora da classe.

## 🧱 Método `__init__`

O método `__init__` é executado automaticamente quando um novo objeto é criado.

Exemplo:

```python
restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
```

Nesse momento, o Python executa o `__init__` e inicializa os atributos do restaurante.

## 🖨️ Método `__str__`

O método `__str__` define como o objeto será representado quando convertido para texto.

```python
def __str__(self):
    return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {self.status}'
```

Isso permite fazer:

```python
print(restaurante_ragazzo)
```

e obter uma representação mais amigável do objeto.

## 🏷️ `@classmethod`

O método:

```python
@classmethod
def listar_restaurantes(cls):
```

é um **método da classe**, pois recebe `cls` em vez de `self`.

Ele pode ser chamado diretamente pela classe:

```python
Restaurante.listar_restaurantes()
```

Sua responsabilidade é percorrer a lista de restaurantes armazenada no atributo de classe:

```python
for restaurante in cls.restaurantes:
    print(restaurante)
```

### `self` x `cls`

Uma das coisas praticadas neste projeto é a diferença entre:

```python
self
```

e:

```python
cls
```

* `self` → representa uma **instância/objeto**.
* `cls` → representa a **classe**.

## ⚙️ `@property`

A propriedade:

```python
@property
def status(self):
    return 'Ativado✅' if self._status else 'Desativado❎'
```

permite acessar o método como se fosse um atributo:

```python
restaurante.status
```

em vez de:

```python
restaurante.status()
```

Isso é útil quando queremos apresentar um valor calculado ou controlado pela classe de uma maneira semelhante ao acesso de um atributo.

## 🚀 Exemplo de utilização

```python
restaurante_ragazzo = Restaurante('Ragazzo', 'Fritos')
restaurante_sujinho = Restaurante('Sujinho', 'Churrasco')

Restaurante.listar_restaurantes()
```

Saída esperada:

```text
Restaurante           | Categoria             | Status
Ragazzo               | FRITOS                | Desativado❎
Sujinho               | CHURRASCO             | Desativado❎
```

## 🎯 Objetivo do projeto

Este projeto faz parte dos meus estudos de **OOP em Python**.

A ideia é começar com uma implementação simples e evoluir o projeto conforme novos conceitos forem aprendidos, como:

* Herança
* Polimorfismo
* Abstração
* Métodos estáticos
* Getters e setters
* Tratamento de exceções
* Organização em módulos
* Testes automatizados

---

### 🧠 O que estou aprendendo

> O principal objetivo não é criar um sistema completo de restaurantes, mas utilizar um problema simples para entender como a **Programação Orientada a Objetos funciona na prática em Python**.

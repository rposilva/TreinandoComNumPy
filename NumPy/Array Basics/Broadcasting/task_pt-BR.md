## Broadcasting

Uma situação frequente é quando temos um array menor e um array maior e precisamos usar o menor para executar alguma operação (por exemplo, adicionar elementos) no maior várias vezes.

O termo [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) descreve como o NumPy trata arrays com formas diferentes durante operações aritméticas. O array menor é "transmitido" ao longo do array maior para que eles tenham formas compatíveis.

Suponha que queremos adicionar um vetor constante 
```python
v = np.array([1, 0, 1])
```

a cada linha de uma matriz 
```python
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
```
Poderíamos fazer isso utilizando um loop `for`. No entanto, quando a matriz é muito grande, computar um loop explícito em Python pode ser lento.

Adicionar o vetor `v` a cada linha da matriz `x` é equivalente a formar primeiro uma matriz `vv` empilhando múltiplas cópias de `v` verticalmente:

```python
vv = np.tile(v, (4, 1))   # Empilha 4 cópias de v uma sobre a outra
print(vv)                 # Imprime "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
```

e depois realizar a soma elemento a elemento de `x` e `vv`. O broadcasting do NumPy nos permite realizar essa computação sem realmente criar múltiplas cópias de `v`. Considere a seguinte solução, que usa broadcasting:

```python
y = x + v  # Adiciona v a cada linha de x usando broadcasting
print(y)  # Imprime "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"
```

O broadcasting fornece um meio de vetorizar operações de array para que o loop ocorra em C ao invés de em Python. Ele faz isso sem criar cópias desnecessárias dos dados e geralmente leva a implementações de algoritmos eficientes. Devido ao broadcasting, a linha `y = x + v` funciona mesmo que `x` tenha a forma `(4, 3)` e `v` tenha a forma `(3,)`. Ela funciona como se `v` realmente tivesse a forma `(4, 3)`, onde cada linha era uma cópia de `v` e a soma era realizada elemento a elemento.

### Regras gerais de broadcasting

- Duas dimensões são compatíveis quando são iguais ou uma delas é 1. Quando qualquer uma das dimensões comparadas é um, a outra é usada. Em outras palavras, dimensões com tamanho 1 são esticadas ou "copiadas" para corresponder à outra.
  
- O tamanho do array resultante é o tamanho que não é 1 ao longo de qualquer eixo das entradas.
  
- Arrays não precisam ter o mesmo número de dimensões. Por exemplo, se você tem um array 256 x 256 x 3 de valores RGB e quer escalar cada cor em uma imagem por um valor diferente, você pode multiplicar a imagem por um array unidimensional com 3 valores.
  
Aqui estão alguns exemplos:

```text
    A      (2d array):  5 x 4
    B      (1d array):      1
    Resultado (2d array):  5 x 4
    
    A      (2d array):  5 x 4
    B      (1d array):      4
    Resultado (2d array):  5 x 4
    
    A      (3d array):  15 x 3 x 5
    B      (3d array):  15 x 1 x 5
    Resultado (3d array):  15 x 3 x 5
    
    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 5
    Resultado (3d array):  15 x 3 x 5
    
    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 1
    Resultado (3d array):  15 x 3 x 5
```
Algumas formas que não realizam broadcasting:
```text
    A      (1d array):  3
    B      (1d array):  4 # dimensões finais não combinam
    
    A      (2d array):      2 x 1
    B      (3d array):  8 x 4 x 3 # penúltimas dimensões não combinam
```

### Tarefa
No editor de código, adicione duas linhas modificando os arrays `x` e `w` de modo que as duas instruções `print` não produzam erros quando o código for executado.

<div class="hint">Use <code>reshape</code>.</div>
## Remodelar

Remodelar significa mudar a `forma` de um array sem alterar seus dados. Como mencionamos anteriormente, a `forma` de um array é o número de elementos em cada dimensão. Ao remodelar, podemos adicionar ou remover dimensões, ou mudar o número de elementos em cada dimensão.

A função [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape) é usada para remodelagem; ela aceita três argumentos:

- O array a ser remodelado.
- A nova forma como um `int` ou tupla de valores `int`.
- Um argumento opcional `order`, que define a ordem na qual os elementos são lidos e colocados no array remodelado.

### Exemplos
1. Remodelar um array 1D em um array 2D:
```python
a = np.arange(10)
print(np.reshape(a, (2, 5)))
```
Saída:
```text
[[0 1 2 3 4]
 [5 6 7 8 9]]
```
2. Remodelar um array 2D em um array 1D:
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.reshape(a, 6))
```
Saída:
```text
[1 2 3 4 5 6]
```

Este último também pode ser conseguido utilizando [`numpy.ndarray.flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html), que retorna uma cópia do array achatada em uma dimensão:
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.flatten())
```
Saída:
```text
[1 2 3 4 5 6]
```

### Tarefa
1. Crie um array `a` de inteiros no intervalo de `12` a `30` com passo `3`.
2. Remodele-o de forma que tenha 2 linhas e 3 colunas.

<div class="hint">Para (1) você pode usar a função <code>arange</code>.</div>
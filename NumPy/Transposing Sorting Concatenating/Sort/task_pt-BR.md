## Ordenação

Os métodos [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html?highlight=sort#numpy.sort) 
e [`numpy.ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort) podem ambos ser usados para ordenar um array, 
a única diferença é que o primeiro retorna uma cópia ordenada de um array, enquanto o último é usado 
para ordenar no local.

<details>

Diversos algoritmos de ordenação podem ser usados com esses métodos (veja a documentação); eles diferem em 
sua velocidade média, desempenho no pior caso, tamanho do espaço de trabalho e estabilidade.
O padrão é [quicksort](https://en.wikipedia.org/wiki/Quicksort).
</details> 

```python
a = np.array([[1, 4], [3, 1]])
print(np.sort(a))               # Ordena ao longo do último eixo por padrão. Retorna uma cópia!
print(np.sort(a, axis=None))    # Ordena o array achatado
print(np.sort(a, axis=0))       # Ordena ao longo do primeiro eixo
```
Saída:
```text
[[1 4]      
 [1 3]]
[1 1 3 4]  
[[1 1]      
 [3 4]]
```
Por outro lado, se usarmos `numpy.ndarray.sort`, obtemos:
```python
a = np.array([[1, 4], [3, 1]])
a.sort(axis=1)      # Ordena no local ao longo do segundo eixo. Equivalente a `a.sort()`
print(a)
a.sort(axis=0)      # Ordena no local ao longo do primeiro eixo
print(a)
```
Saída:
```text
[[1 4]
 [1 3]]
[[1 3]
 [1 4]]
```
A diferença nos resultados vem do fato de que o primeiro método `numpy.sort` retorna uma cópia de um array, enquanto
o segundo (`numpy.ndarray.sort`) modifica o array inicial. Ou seja, no exemplo acima, classificamos os elementos de um array, primeiro nas linhas, depois nas colunas.

### Ordenação indireta
Ao contrário dos métodos discutidos acima, o método [`numpy.argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort) retorna os **índices**
que ordenariam um array.
Ele realiza uma ordenação indireta ao longo do eixo fornecido e retorna um array de índices (da 
mesma forma que o array de entrada) que indexa os dados ao longo do eixo especificado em ordem classificada.

Para um array 1D:
```text
x = np.array([3, 1, 2])
print(np.argsort(x))
```
Saída:
```text
[1 2 0]
```
Para um array 2D:
```python
y = np.array([[0, 3], [2, 1]])
ind = np.argsort(y, axis=0)  # Ordena ao longo do primeiro eixo (para baixo)
print(ind)
print(np.take_along_axis(y, ind, axis=0))  # Igual a np.sort(x, axis=0)
```
Saída:
```text
[[0 1]
 [1 0]]
[[0 1]
 [2 3]]
```
Continuando o último exemplo:
```python
ind2 = np.argsort(y, axis=1)  # Ordena ao longo do último eixo (horizontalmente)
print(ind2)
print(np.take_along_axis(y, ind2, axis=1))  # Igual a np.sort(x, axis=1)
```
Saída:
```text
[[0 1]
 [1 0]]
[[0 3]
 [1 2]]
```
`argsort` é uma funcionalidade de ordenação frequentemente usada em trabalhos intensivos de código com dados. Ela aumenta a velocidade de 
cálculo, especialmente quando os conjuntos de dados são muito grandes.

A função [`numpy.take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html)
toma valores do array de entrada usando um array de índices. Isto é necessário sempre que você
trabalhar com funções NumPy como `argsort`, [`argpartition`](course://Numpy/Transposing Sorting Concatenating/Partial Sort) e [`argmax`](course://Numpy/Compare Search/Find maximum), que 
retornam um array de índices que podem ser usados posteriormente para ordenar o array inicial ou realizar outra operação 
com ele.

### Tarefa
Você recebe um array 2D de 100 inteiros aleatórios.
1. Ordene as colunas (segundo eixo!) deste array e atribua o resultado à variável `b`.
2. Encontre os índices para ordenar as linhas do array `b` e atribua o resultado a `ind`.
3. Ordene completamente o array usando esses índices. Consulte os exemplos acima.
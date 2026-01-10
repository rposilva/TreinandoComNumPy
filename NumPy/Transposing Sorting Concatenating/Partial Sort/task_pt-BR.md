## Ordenação parcial (Partição)

Se você tem um conjunto de dados na forma de um array do NumPy e deseja apenas obter os `k` menores números dele, em vez de ordená-lo completamente, essa tarefa pode ser realizada utilizando o método [`numpy.partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition). Isso é chamado de **ordenação parcial** porque estaremos ordenando apenas algumas partes do array, o que significa que obteremos uma **partição** dos `k` menores valores.

`numpy.partition()` cria uma cópia do array com seus elementos rearranjados de tal forma que o elemento na posição k estará onde estaria em um array ordenado. Todos os elementos menores que o elemento na posição k são movidos antes desse elemento, e todos os elementos **iguais ou maiores** são movidos para depois dele. A ordem dos elementos nas duas partições é indefinida.

O método aceita o array a ser ordenado e um índice de elemento para parti-lo. No exemplo abaixo, o conjunto de dados de 10 inteiros é particionado pelo 5º elemento:

```text
a = np.array([6, 0, 5, 2, 17, 2, 10, 17, 0, 13])
b = np.partition(a, 4)
print(a, '\n', b)
```
Saída (o sinal ^ indica o elemento pelo qual o array foi particionado):
```text
[ 6  0  5  2 17  2 10 17  0 13] 
[ 0  0  2  2  5  6 10 13 17 17]
              ^
```
### Ordenação parcial indireta

Assim como na ordenação regular, a ordenação parcial pode ser realizada de forma indireta. A função `numpy.argpartition()` cria uma partição indireta pelo parâmetro k ao longo do eixo dado. Ela retorna um **array de índices** da mesma forma que o array pai na ordem particionada.

```python
x = np.array([8, 3, 4, 2, 1, 7, 0, 10, 5])
print(np.argpartition(x, 4))
print(x[np.argpartition(x, 4)])
```
Saída:
```text
[3 6 4 1 2 8 5 7 0]
[ 2  0  1  3  4  5  7 10  8]
              ^
```
Em 2-D:
```python
x = np.array([[3, 4, 2, 5, 0], [1, 3, 1, 2, 0]])
index_array = np.argpartition(x, kth=2, axis=-1)
print(np.take_along_axis(x, index_array, axis=-1))  # igual a np.partition(x, kth=1)
```
Saída:
```text
[[0 2 3 5 4]
 [0 1 1 2 3]]
```
### Tarefa
Você tem um array `arr` com 20 números aleatórios e um valor-alvo `target`. Você precisa encontrar `k = 3` pontos de dados no array `arr` que estejam mais próximos de `target` em valor. O array `differences` contém as distâncias entre `target` e cada elemento de `arr`.
1. Obtenha os índices de `differences` particionados pelo elemento k.
2. Reorganize `arr` usando esses índices e
3. Obtenha apenas `k` elementos mais próximos de `target`.

<div class="hint">Veja exemplos na descrição da tarefa para 1 e 2. Use fatiamento para 3.</div>
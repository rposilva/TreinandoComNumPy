## Concatenar

Concatenação refere-se a juntar duas ou mais matrizes da mesma forma ao longo de um eixo especificado. 
Embora exista [`numpy.concatenate()`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html), 
também há várias funções auxiliares que às vezes são mais fáceis de ler.

`numpy.concatenate()` é usado para juntar uma sequência de matrizes ao longo de um eixo existente. 
Aceita uma sequência de matrizes da mesma forma exceto na dimensão especificada pelo parâmetro opcional 
`axis`, que é o eixo ao longo do qual as matrizes serão unidas. Se `axis` for `None`, as matrizes são achatadas antes do uso. 
O valor padrão é `0`. A função retorna a matriz concatenada.

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[0, 0, 0]])
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b.T), axis=1))
print(np.concatenate((a, b), axis=None))
```
Saída:
```text
[[1 2 3]
 [4 5 6]
 [7 8 9]
 [0 0 0]]
[[1 2 3 0]
 [4 5 6 0]
 [7 8 9 0]]
[1 2 3 4 5 6 7 8 9 0 0 0]
```
### Empilhar
1. [`numpy.stack()`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack) junta 
uma sequência de matrizes ao longo de um **novo eixo**. O parâmetro `axis` especifica o índice do novo eixo nas 
dimensões do resultado. Por exemplo, se `axis=0`, será a primeira dimensão e se `axis=-1`, 
será a última dimensão.

```python
a = np.array([[1, 2], [3, 4]])
print(np.stack((a, a), axis=0))
print(np.stack((a, a), axis=-1))
```
Saída:
```text
[[[1 2]
  [3 4]]
 [[1 2]
  [3 4]]]
  
[[[1 1]
  [2 2]]
 [[3 3]
  [4 4]]]
```
2. [`numpy.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) empilha 
matrizes em sequência horizontalmente (por coluna). 
Isso é equivalente à concatenação ao longo do segundo eixo, exceto para matrizes 1D, onde concatena ao longo do primeiro eixo:
```python
a, b = np.array((1, 2, 3)), np.array((4, 5, 6))
print(np.hstack((a, b)))
c, d = np.array([[1], [2], [3]]), np.array([[4], [5], [6]])
print(np.hstack((c, d)))
```
Saída:
```text
[1 2 3 4 5 6]
[[1 4]
 [2 5]
 [3 6]]
```
3. [`numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack) empilha 
matrizes em sequência verticalmente (por linha). Isso é equivalente à concatenação ao longo do primeiro eixo 
após matrizes 1D de forma `(N,)` terem sido remodeladas para `(1, N)`.
```python
a, b = np.array((1, 2, 3)), np.array((4, 5, 6))
print(np.vstack((a, b)))
c, d = np.array([[1], [2], [3]]), np.array([[4], [5], [6]])
print(np.vstack((c, d)))
```
Saída:
```text
[[1 2 3]
 [4 5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
```

### Tarefa
1. Você tem uma matriz de zeros `a` de formato `(3, 4)`. Crie uma matriz `b` de forma que 
ao concatená-la apropriadamente com `a`, você obtenha:
```text
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 1 2 3]]
```
2. Use um dos métodos de empilhamento para criar uma matriz `empilhada`:
```text
[[ 0  1  2  3  4  5  6  7  8  9]
 [20 21 22 23 24 25 26 27 28 29]
 [40 41 42 43 44 45 46 47 48 49]]
```
<div class="hint">Use <code>np.arange</code> para <code>b</code> e não esqueça de 
remodelar a matriz apropriadamente! Além disso, tenha em mente o eixo de concatenação.</div>
<div class="hint">A tarefa com <code>empilhada</code> pode ser completada em uma linha. Use <code>np.arange</code> para
cada uma das três matrizes iniciais.</div>
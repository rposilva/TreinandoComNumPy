## Transpor

Quando você transpõe um array, a ordem dos eixos é invertida, e os índices de cada elemento são invertidos ao longo de cada eixo. O item `[0, 1]`, por exemplo, torna-se o item `[1, 0]`. [`numpy.ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose) retorna uma visualização do array com os eixos transpostos. Alternativamente, você também pode usar o atributo [`a.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T).

Este método aceita `None` ou uma tupla de `int`s. No caso de `None` ou nenhum argumento, inverte a ordem dos eixos. No caso de uma tupla de `int`s, `i` na posição `j` na tupla significa que o eixo `i` de `a` se torna o eixo `j` de `a.transpose()`. Para ilustrar:

```python
a = np.arange(15).reshape(3, 5)
print(a.transpose())
print(a.T)
print(a.transpose(1, 0))
```
Saída (todas produzem a mesma coisa):
```text
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
```

> <i>O método [`numpy.ndarray.reshape`](course://Numpy_/Array Basics/Reshape) que encontramos anteriormente
atribui uma nova forma a um array sem alterar seus dados e também pode ser usado para transposição.</i>

<details>A operação de transposição torna-se mais complexa quando lidamos com arrays de dimensões mais altas, como arrays 3D. No caso de arrays 3D, a operação de transposição envolve permutar os eixos com base no parâmetro de eixos fornecido.</details>

### Tarefa 
1. Transpor o array `a`.
2. Transformar o array `b` de modo que ele fique assim:
```text
   [[0 1 2]
   [3 4 5]
   [6 7 8]]
```
3. Usar os métodos do numpy `arange`, `reshape`, e `transpose` para obter um array 3D `c` que fique assim:
```text
[[[ 0  4  8]
  [ 2  6 10]]

 [[ 1  5  9]
  [ 3  7 11]]]
```

<div class="hint">Você pode usar tanto <code>a.T</code> quanto <code>a.transpose()</code> para os dois primeiros arrays.</div>

<div class="hint">No item #3, use os métodos na ordem sugerida. Você pode fazer isso em uma linha de código.</div>
## Comparação Elemento a Elemento

A comparação elemento a elemento é quando você compara cada elemento de um array com um elemento de outro array. [`numpy.equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html) é uma função que retorna `(x1 == x2)` elemento a elemento. Ela aceita dois arrays de entrada que devem ter o mesmo `shape` ou serem transmissíveis para um shape comum (que se torna o shape da saída). Elementos do array resultante são tipicamente valores booleanos.

Exemplo:
```python
print(np.equal([0, 1, 3], np.arange(3)))
```
Saída:
```text
[ True,  True, False]
```
O que é comparado são valores, não tipos. Assim, um int (1) e um array de comprimento um podem avaliar como `True`:
```python
print(np.equal(1, np.ones(1)))
```
Saída:
```text
[ True]
```
O operador `==` pode ser usado como uma forma abreviada para `np.equal` em ndarrays.

### `numpy.array_equal`

[`numpy.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html) é uma função que retorna `True` se dois arrays de entrada têm **o mesmo shape e elementos** e `False` caso contrário.

Exemplos:
```python
print(np.array_equal([1, 2], [1, 2]))
print(np.array_equal(np.array([1, 2]), np.array([1, 2])))
print(np.array_equal([1, 2], [1, 2, 3]))
print(np.array_equal([1, 2], [1, 4]))
```
Saída:
```text
True
True
False
False
```

### Tarefa
Defina um array **1D** `b` de tal forma que, comparando-o elemento a elemento com o array `a`, você obtenha o array `compare_a_b`, que é `array_equal` (tem os mesmos elementos e shape) ao array no último comando `print`. Quando você executar o script, o último comando `print` deve imprimir `True`.

<div class="hint">O array <code>b</code> deve ter shape <code>(5,)</code>. Use <code>np.arange</code> com os argumentos <code>start</code>, <code>stop</code> e <code>step</code>. Observando o array booleano resultante, você poderá determinar qual inteiro deve estar em qual posição em <code>b</code> e, então, elaborar argumentos adequados para a função <code>np.arange</code>.</div>

<div class="hint">Para obter o array <code>compare_a_b</code>, use a função <code>np.equal</code>.</div>
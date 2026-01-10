## Criar um Array Vazio

Às vezes, o tamanho de um array é conhecido, enquanto seus elementos são originalmente desconhecidos. 
O NumPy oferece várias funções para criar arrays com conteúdo inicial de espaço reservado:

- a função [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros) cria um array cheio de zeros;
- a função [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html?highlight=ones#numpy.ones) cria um array cheio de uns;
- a função [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty) cria um array onde o conteúdo inicial é aleatório e 
depende do estado da memória.

<details>

Por padrão, o `dtype` de um array criado desta forma é [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html?highlight=float64#numpy.float64), 
mas pode ser especificado de outra forma com o argumento `dtype`.
</details>

```python
a = np.zeros((3, 4))
b = np.ones((2, 3), dtype=np.int16)
c = np.empty((2, 3))

print(a)
print(b)
print(c)
```
Saída:
```text
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[1 1 1]
 [1 1 1]]
[[2.31584178e+077 2.31584178e+077 1.97626258e-323]
 [3.95252517e-323 1.18575755e-322 3.95252517e-323]]
```

Outra função, [`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full), 
retorna um novo array de uma forma e tipo dados preenchido com um valor especificado.

```python
a = np.full((2, 2), 10)
print(a)
```
Saída:
```text
[[10, 10],
 [10, 10]]
```

### Tarefa
Complete a implementação da função `create_arrays()` para criar os arrays `a` e `b`, onde:
- o array `a` contém apenas os valores `1` com `dtype` `int64` (ou `int`);
- o array `b` contém apenas os valores `True`.
Ambos os arrays devem ter a forma `(x, y)`.

<div class="hint">Para <code>a</code>, use a função <code>numpy.ones</code>.</div>
<div class="hint">Para <code>b</code>, use a função <code>numpy.full</code>.</div>
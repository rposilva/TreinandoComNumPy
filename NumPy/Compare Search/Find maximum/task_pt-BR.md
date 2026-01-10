## Encontrar o Máximo (ou Mínimo)

Existem várias maneiras de encontrar o valor máximo em um array. A maneira mais simples é usar [`numpy.amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html), que retorna o máximo de um array ou o máximo ao longo de um eixo:

```python
a = np.array([[0, 1], [2, 3]])
print(np.amax(a))          # Máximo do array achatado
print(np.amax(a, axis=0))  # Máximos ao longo do primeiro eixo
print(np.amax(a, axis=1))  # Máximos ao longo do segundo eixo
```
Saída:
```text
3
[2 3]
[1 3]
```
Às vezes, pode ser útil saber o índice do elemento máximo. Nesse caso, você pode usar [`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html), que retorna os índices dos valores máximos ao longo de um eixo:

```python
a = np.array([[10, 11, 12], [13, 14, 15]])
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
```
Saída:
```text
5
[1 1 1]
[2 2]
```
Caso você precise realizar uma comparação elemento a elemento entre dois arrays de forma igual (ou passíveis de broadcast para uma forma comum), [`numpy.maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html) é a função adequada. Ela compara dois arrays e retorna um novo array contendo os máximos elemento a elemento. Se os dois arrays de entrada forem passíveis de broadcast para uma forma comum, essa forma se torna a forma de saída.

```python
print(np.maximum([100, 0, 7], [99, 5, 2]))
```
Saída:
```text
[100   5   7]
```

As funções [`numpy.amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin), 
[`numpy.argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin), e 
[`numpy.minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum) fornecem funcionalidades simétricas para encontrar mínimos.

### Tarefa
1. Importe dados do arquivo `data.csv` em um array; `dtype` deve ser `np.int64`.
2. Encontre os índices dos valores máximos em cada linha.
3. Use esses índices para extrair os elementos máximos de cada linha e atribua o array resultante à variável `result`. Por favor, use exatamente esse nome.

Você pode adicionar quaisquer declarações `print` que desejar no bloco `main` para ajudá-lo a realizar esta tarefa.

<div class="hint">
Para o item (3), você precisará da função <code>numpy.take_along_axis</code>, que discutimos na tarefa "Ordenar".
</div>

<div class="hint">
Note a forma do array de índices. Para usá-lo com <code>numpy.take_along_axis</code> para extrair os elementos máximos dos
dados, ele precisa ser reformulado. Você poderia usar <code>numpy.reshape</code> e especificar a forma desejada, ou usar outra função,
<a href="https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html"><code>numpy.expand_dims(a, axis)</code></a>,
nesse caso você não precisa especificar a forma desejada.
</div>
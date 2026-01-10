## bincount

Um caso de uso um tanto relacionado a encontrar valores únicos é contar o número de ocorrências de cada valor em um array. A função [`numpy.bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html) faz exatamente isso para um array de inteiros não negativos. Ela retorna o resultado da binagem do array de entrada, que é a contagem de quantas vezes cada inteiro no intervalo de 0 até o valor máximo no array de entrada é encontrado no array de entrada. Portanto, o número de bins (de tamanho 1) é um a mais que o maior valor no array de entrada.

```python
a = np.array([1, 1, 1, 2, 3, 7, 7])
print(np.bincount(a))
```
Saída:
```text
[0 3 1 1 0 0 0 2]
```
[`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) é um pouco semelhante, mas permite tamanhos de bins variáveis. Você pode especificar o número de bins (`bins=10` por padrão) e `range`, que é `(a.min(), a.max())` por padrão. A função retorna dois arrays: os valores do histograma e as bordas dos bins. Ela também pode retornar o valor da função densidade de probabilidade em cada bin (normalizada de modo que o integral sobre o intervalo seja 1) em vez do número de amostras no bin se você usar o argumento `density=True`.

Usando o array `a` que definimos anteriormente, obtemos:
```python
bincounts = np.bincount(a)
hist, _ = np.histogram(a, range=(0, a.max()), bins=a.max() + 1)
print(np.array_equal(hist, bincounts))
```
Saída:
```python
True
```
Se o array de entrada for multidimensional, o histograma é calculado sobre o array achatado.

### tarefa

Usando algumas das funções que você aprendeu nesta e em tarefas anteriores, encontre a classe mais frequente nos dados.

<div class="hint">Pode ser útil usar o <code>np.bincount</code> nos rótulos das classes.</div>
<div class="hint">Quando você tiver o array binned, a única coisa que resta fazer é pegar a classe mais populosa usando uma das funções para encontrar máximos que discutimos anteriormente.</div>
## Busca

Você pode buscar um array por um certo valor ou por valores que satisfaçam uma condição e retornar os **índices** que correspondam.

Você pode utilizar o método [`numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html):

```python
a = np.array([0, 10, 4, 11, 7, 3])
print(np.nonzero(a < 5))
print(np.nonzero(a == 7))
print(a < 5)
```
Saída:
```text
(array([0, 2, 5]),)
(array([4]),)
[ True False  True False False  True]
```
`numpy.nonzero` retorna os índices dos elementos que não são zero. Um uso comum para ele é encontrar os índices de um array onde uma condição é `True`. Para o array `a`, a condição `a < 5` é um array booleano (veja o exemplo acima). `False` é interpretado como `0`, portanto, `np.nonzero(a < 5)` fornece os índices de `a` onde a condição é verdadeira. Usar o resultado para indexar `a` (`a[np.nonzero(a < 5)]`) é equivalente a usar a máscara diretamente (`a[a < 5]`), e esta última é a forma preferida.

`np.nonzero(a < 5)` é equivalente a `np.where(a < 5)` (que também retorna os índices dos elementos no array de entrada onde a condição é satisfeita):

```python
print(np.where(a < 5))
```
Saída:
```text
(array([0, 2, 5]),)
```
No entanto, [`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) também pode ser usado de uma forma diferente: se fornecido com uma condição e dois arrays de entrada, `numpy.where(condition[, x, y])` retorna **elementos** (não índices) escolhidos de `x` ou `y` dependendo da condição:

```python
a = np.array([0, 0, 0, 0, 0, 5, 6, 7, 8, 9])
b = a * 10
print(np.where(a < 5, a, b))
```
Saída:
```text
[ 0  0  0  0  0 50 60 70 80 90]
```

Na verdade, o primeiro argumento aceito por essa função também é um array – um array booleano, `a < 5` neste caso. Portanto, ele também pode ser usado assim:

```python
result = np.where([False, True, False], [1, 1, 1], [7, 8, 9])
print(result)
```
Saída:
```text
[7 1 9]
```
Os arrays `x`, `y` e `condição` precisam ser compatíveis em termos de forma.

### Tarefa

Você recebe um array de números inteiros aleatórios entre 0 e 25 representando temperaturas registradas em certos dias da semana. Usando a funcionalidade que você acabou de aprender, gere um array `result`, que contém strings, `Low` ou `High`, em uma ordem dependendo de se o dia correspondente da semana foi mais quente do que 15 graus (`High`) ou não (`Low`). Você provavelmente precisará definir dois arrays adicionais, `high` e `low`, contendo strings que serão usadas para `result`.

Além disso, `warm_days` deve conter os nomes dos dias quentes (com temperaturas acima de 15).

<div class="hint"><code>result</code> deve parecer algo como <code>['High' 'Low' 'Low' 'Low' 'High' 'High' 'High']</code>.</div>

<div class="hint">Use <code>numpy.where</code> com uma condição sobre temperaturas e dois arrays de entrada <code>high</code> e <code>low</code> para obter o <code>result</code>.</div>

<div class="hint">Para a última parte, use <code>numpy.nonzero</code> ou uma máscara direta.</div>
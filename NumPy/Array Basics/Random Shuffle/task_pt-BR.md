## Embaralhamento Aleatório

Às vezes, você precisa embaralhar o conteúdo de um array. Por exemplo, em tarefas de aprendizado de máquina, é comum embaralhar e normalizar os dados.

O NumPy oferece dois métodos que fornecem dados embaralhados aleatoriamente (ou **permutados**):
- [`random.Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation) permuta aleatoriamente uma sequência ou retorna um intervalo permutado.
- [`random.Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle) modifica um array ou sequência **in-place** ao embaralhar seu conteúdo.

A principal diferença entre esses dois métodos é que `permutation` retorna um array, enquanto `shuffle` o modifica in-place. Além disso, `permutation` permite criar uma sequência permutada a partir de um intervalo. Para arrays com mais de uma dimensão, a ordem dos sub-arrays é alterada, mas seu conteúdo permanece o mesmo. Confira os exemplos abaixo.

1. Embaralhar / permutar uma sequência
```python
rng = np.random.default_rng()
print(rng.permutation(10))  # Permutação retorna um intervalo permutado
```
Saída (será diferente a cada vez):
```text
[6 5 0 4 9 1 8 2 3 7]
```

```python
arr = np.arange(10)
rng.shuffle(arr)  # Embaralha a sequência in-place
print(arr)
```
Saída:
```text
[0 3 5 7 8 6 9 1 2 4]
```
2. Embaralhar / permutar um array 2D
```python
arr = np.arange(9).reshape((3, 3))
print(rng.permutation(arr))  # Permutação retorna um array permutado, a ordem dentro das linhas permanece a mesma
```
Saída:
```text
[[3 4 5]
 [6 7 8]
 [0 1 2]]
```
```python
arr = np.arange(9).reshape((3, 3))
rng.shuffle(arr)  # Embaralha o array in-place, a ordem dentro das linhas permanece a mesma
print(arr)
```
Saída:
```text
[[6 7 8]
 [3 4 5]
 [0 1 2]]
```
2. Embaralhar / permutar um array 2D ao longo de outro eixo
```python
arr = np.arange(9).reshape((3, 3))
print(rng.permutation(arr, axis=1))  # Permutação retorna um array permutado dentro das linhas
```
Saída:
```text
[[2 0 1]
 [5 3 4]
 [8 6 7]]
```
```python
arr = np.arange(9).reshape((3, 3))
rng.shuffle(arr, axis=1)  # Embaralha o array in-place dentro das linhas
print(arr)
```
Saída:
```text
[[0 2 1]
 [3 5 4]
 [6 8 7]]
```

### Tarefa

Primeiro, `shuffle` as linhas do array `arr` (o eixo 0 é o eixo padrão). Em seguida, permute aleatoriamente os números dentro das linhas em `arr` e atribua o resultado à variável `permuted_2d`. Ainda assim, seu array não está totalmente aleatório, pois todos os elementos permanecem nas mesmas linhas onde estavam. Crie um array `fully_random`. Use alguns dos métodos que aprendemos anteriormente.

<div class="hint">Use os exemplos na descrição da tarefa para embaralhar e permutar o array.</div>

<div class="hint">Para randomizá-lo completamente, você poderia primeiro <code>flatten</code> o array, então aplicar o método <code>permutation</code> nele, e <code>reshape</code> de volta à forma original. Todas essas coisas podem ser feitas em uma linha de código (embora isso não signifique que sempre deva ser assim).</div>
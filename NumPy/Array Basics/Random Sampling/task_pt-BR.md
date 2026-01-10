## Amostragem aleatória

Às vezes, pode ser necessário preencher uma matriz com números aleatórios ou amostrá-los de diferentes distribuições estatísticas. O módulo [`random`](https://numpy.org/doc/stable/reference/random/#module-numpy.random) do Numpy permite que você faça isso. É um conjunto de funções baseado na [geração de números pseudorrandômicos](https://en.wikipedia.org/wiki/Pseudorandom_number_generator). É chamado de pseudorrandômico porque "aleatório" significa algo que não pode ser previsto logicamente, e se um programa gera um número "aleatório" que pode ser previsto, ele não é verdadeiramente aleatório.

A função `numpy.random.random` retorna floats aleatórios no [intervalo semiaberto](https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology) `[0.0, 1.0)`:

```python
a = np.random.random(5)
print(a)
```
Saída:
```text
[0.73719247 0.38265166 0.48330973 0.27551432 0.88136674]
```

### Gerador aleatório

[`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator) é um contêiner que expõe vários métodos para gerar números aleatórios provenientes de uma variedade de distribuições de probabilidade. Chame [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng) para obter uma nova instância de `Generator`, em seguida, chame seus métodos para obter amostras de diferentes distribuições.
```python
rng = np.random.default_rng()
a = rng.integers(1000)  # Escolhe aleatoriamente um inteiro de 0 a 1000
print(a)
```
Saída:
```text
346
```
`random.Generator.integers` retorna inteiros aleatórios de um intervalo semiaberto: baixo (inclusive) a alto (exclusive), ou um intervalo fechado – se você especificar `endpoint=True`: baixo (inclusive) a alto (inclusive). Os inteiros são retornados da distribuição "uniforme discreta".

Imprima 10 inteiros aleatórios do intervalo `[0, 2)`:

```python
print(rng.integers(2, size=10)) 
```
Saída:
```text
[1 1 0 1 0 0 0 1 0 0]
```
Gere uma matriz de 2 x 4 de inteiros entre `0` e `4`, inclusive:
```python
print(rng.integers(4, size=(2, 4), endpoint=True))
```
Equivalente a:
```python
print(rng.integers(5, size=(2, 4)))
```
Saída:
```text
[[1 2 0 3]
 [4 2 4 3]]
```

### Tarefa
Usando a função [`numpy.random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html?highlight=random%20normal#numpy.random.Generator.normal), extraia 1000 amostras da distribuição normal com a média igual a `1` e desvio padrão igual a `0.5`. Você pode visualizar sua amostra e certificar-se de que a média e a variância estão corretas executando o script – nós predefinimos o código para isso no bloco `main`.
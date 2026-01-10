## Indexação de Arranjos de Inteiros

Arranjos do NumPy podem ser indexados com outros arranjos.
Para todos os casos de arranjos de índice, o que é retornado é uma cópia dos dados originais, não uma visão como se obtém com fatias.

Os arranjos de índice devem ser do tipo inteiro. Cada valor no arranjo indica qual valor no arranjo usar no lugar do índice. Valores negativos são permitidos e funcionam da mesma forma que com índices únicos ou fatias.

```python
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a = np.array([0, 3, 5, 2])
print(x[a])
```
Saída:
```text
[1 4 6 3]
```

Quando arranjos de índice são usados, o que é retornado é um arranjo com a mesma forma do arranjo de índice, mas com o tipo e os valores do arranjo sendo indexado:
```python
b = np.array([[9, 9], [0, 1]])
c = x[b]
print(c)
```
Saída:
```text
[[10 10]
 [ 1  2]]
```

### indexação de arranjos multidimensionais
As coisas se tornam mais complexas quando arranjos multidimensionais são indexados, particularmente com arranjos de índice multidimensionais.
Vamos considerar isto:

```python
x = np.arange(15).reshape(5, 3)
print(x)
print(x[np.array([0, 1, 4])])  # 1
print(x[np.array([0, 1, 4]), np.array([0, 0, 1])])  # 2
```
Saída:
```text
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]]
 
[[ 0  1  2]
 [ 3  4  5]
 [12 13 14]]
 
[ 0  3 13]
```
Você pode ver que no primeiro caso, um novo arranjo é construído, onde cada valor do arranjo de índice seleciona uma linha do arranjo indexado e o arranjo resultante tem a forma `(número_de_elementos_do_índice, tamanho_da_linha)`.

No segundo caso, o arranjo resultante tem a mesma forma que os arranjos de índice, e os valores correspondem ao conjunto de índices para cada posição nos arranjos de índice. Neste exemplo, o primeiro valor de índice é `0` para ambos os arranjos de índice, e assim o primeiro valor do arranjo resultante é `x[0, 0]`. O próximo valor é `y[1, 0]`, e o último é `y[4, 1]`.

Se os arranjos de índice não tiverem a mesma forma, tenta-se transmitir eles para a mesma forma. Se não puderem ser transmitidos para a mesma forma, uma exceção é lançada.

O mecanismo de transmissão permite que arranjos de índice sejam combinados com escalares para outros índices. O valor escalar é usado para todos os valores correspondentes dos arranjos de índice:

```python
x = np.arange(15).reshape(5, 3)
print(x[np.array([0, 2, 3, 4]), 1])
```
Saída:
```text
[ 1  7 10 13]
```
Você pode ler mais sobre indexação de inteiros [aqui](https://numpy.org/doc/stable/reference/arrays.indexing.html#integer-array-indexing).

### tarefa
1. Usando indexação de arranjos de inteiros, crie um arranjo `a` que contenha elementos com índices `[7, 13, 28, 33]` do arranjo `x`.
   Em seguida, crie um arranjo 2D `b` com a forma `(3, 3)` que contenha elementos com índices `[0, 1, 2], [10, 11, 12], [28, 29, 30]` do arranjo `x`.

2. Com base no arranjo 2D `y`:
   - Crie um arranjo `c` contendo as linhas número `0`, `2` e `4`.
   - Crie um arranjo 1D `d` contendo os elementos `0`, `1` e `2` das linhas `0`, `2` e `4`, respectivamente.
   - Crie um arranjo 1D `e` contendo elementos com o índice `6` das linhas `1`, `2` e `4`.
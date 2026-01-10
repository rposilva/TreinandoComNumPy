## Indexação Booleana

Arrays booleanos usados como índices são tratados de forma diferente de arrays de índice. Arrays booleanos devem ter a mesma forma das dimensões iniciais do array que está sendo indexado. Esses arrays booleanos são frequentemente chamados de **máscaras**, e o processo de usá-los na indexação de outros arrays é chamado de mascaramento ou filtragem mascarada.

```python
y = np.arange(20).reshape(5, 4)
b = y % 2 != 0
print(b)
print(y[b])
```
Saída:
```text
[[False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]]
[ 1  3  5  7  9 11 13 15 17 19]
```
Ao contrário do caso de arrays de índices inteiros, no caso booleano, o resultado é um array 1D contendo todos os elementos no array indexado correspondentes a todos os elementos verdadeiros no array booleano. Assim como com arrays de índice, o que é retornado é uma cópia dos dados, não uma visão como se obtém com fatias.

O resultado será multidimensional se `y` tiver mais dimensões do que `b`. Por exemplo, se usarmos um array booleano 1D onde a segunda dimensão concorda com a de `b` (apenas selecionando uma linha de `b`), então as colunas de `y` correspondentes aos valores `True` no array 1D serão selecionadas:
```python
print(b[1, :])
print(y[:, b[1, :]])
```
Saída:
```text
[False  True False  True]
[[ 1  3]
 [ 5  7]
 [ 9 11]
 [13 15]
 [17 19]]
```
As 2ª e 4ª colunas são selecionadas do array indexado e combinadas para formar um array 2D.

Em geral, quando o array booleano tem menos dimensões do que o array indexado, a forma do resultado é uma dimensão contendo o número de elementos `True` do array booleano seguido pelas dimensões restantes do array indexado.

Para mais detalhes, consulte a documentação de referência do NumPy sobre [indexação de arrays](https://numpy.org/doc/stable/reference/arrays.indexing.html#indexing).

### Tarefa 
1. Crie um array 3D `a` com inteiros de 0 a 19 e forma `(2, 2, 5)`.
2. Filtre-o usando um array booleano 2D `b` para que o array 2D resultante `c` tenha a forma `(2, 5)` e contenha os elementos `[ 0  1  2  3  4]` e `[15 16 17 18 19]`.
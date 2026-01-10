## Transpor um array 1D

Em termos de linguagens de programação, não é possível transpor um array 1D: a transposição de um array 1D ainda é um array 1D.

Um array 1D é uma linha de uma matriz. Se precisarmos transpô-lo, devemos converter essa matriz 1D para uma matriz 2D e então transpor. Veja o exemplo abaixo para uma ilustração.

```python
a = np.array([0, 10, 20, 30, 40])
b = np.array([[0, 10, 20, 30, 40]])  # Ou: b = a.reshape(1, 5)
print(a)
print(b)
print(a.shape)
print(b.shape)
print(a.T)
print(b.T)
```
Saída:
```text
[ 0 10 20 30 40]
[[ 0 10 20 30 40]]
(5,)
(1, 5)
[ 0 10 20 30 40]
[[ 0]
 [10]
 [20]
 [30]
 [40]]
```
A transposição do array 1D é a mesma que o próprio array, mas a transposição do array 2D é algo completamente diferente.

### Tarefa
Implemente a função `reshape_transpose`, que aceita três parâmetros: `start`, `stop` e `step`, gera um array 1D usando `arange`, e retorna um array transposto.
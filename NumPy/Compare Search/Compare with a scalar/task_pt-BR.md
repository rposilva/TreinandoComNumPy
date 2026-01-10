## Comparar com um Escalar

Cada elemento de um array pode ser comparado com um escalar usando qualquer um dos operadores:
- maior que (`>`),
- maior ou igual a (`>=`), 
- menor que (`<`), 
- menor ou igual a (`<=`),
- igual a (`==`).

Isso é possível graças ao recurso de [broadcasting](course://NumPy/Array Basics/Broadcasting). 
Por exemplo, a comparação `arr > x` produz um array de valores booleanos resultantes de comparações elemento a elemento:
```python
arr = np.arange(10)
print(arr > 3)
```
Saída:
```text
[False False False False  True  True  True  True  True  True]
```
Você já viu tais arrays na tarefa [Indexação Booleana](course://NumPy/Array Indexing and Slicing/Boolean Indexing).

### Tarefa
Sua tarefa é criar o array `filtered_arr` de forma que ele contenha apenas os números do array original `arr` que são divisíveis por `4`.

<div class="hint">Use indexação booleana.</div>
## Encontrar Valores Únicos

A função [`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) é bastante direta – ela encontra elementos únicos no array de entrada e os retorna como um array ordenado:

```python
print(np.unique([1, 1, 2, 2, 3, 3]))
```
Saída:
```text
[1 2 3]
```
Além disso, `numpy.unique` pode:

- identificar linhas ou colunas únicas de um array (quando o parâmetro `axis` é fornecido, quando não – a busca é realizada no array de entrada **achatado**):

```python
a = np.array([[1, 2, 6], [4, 2, 3], [4, 2, 3]])
print(np.unique(a))
print(np.unique(a, axis=0))
```
Saída:
```text
[1 2 3 4 6]
[[1 2 6]
 [4 2 3]]
```

- retornar os valores únicos e o número de ocorrências de cada valor único (`return_counts=True`):
```python
a = np.array([1, 2, 6, 4, 2, 3, 2])
print(np.unique(a, return_counts=True))
```
Saída:
```text
(array([1, 2, 3, 4, 6]), array([1, 3, 1, 1, 1]))
```

- retornar o índice das primeiras ocorrências dos valores únicos (`return_index=True`):

```python
a = np.array([1, 2, 6, 4, 2, 3, 2])
unique, index = np.unique(a, return_index=True)
print(unique, index)
```
Saída:
```text
[1 2 3 4 6] [0 1 5 3 2]
```
### Tarefa
Você tem um conjunto de dados no arquivo `data.csv`. A primeira coluna contém IDs (rótulos de classe), todas as outras colunas – valores de algumas métricas coletadas para cada entrada.
1. [Carregue o conjunto de dados](course://NumPy/Array Basics/Reading and Writing Files) do arquivo `csv`. Preste atenção no cabeçalho!
2. [Divida](course://NumPy/Array Indexing and Slicing/Indexing Basics) o conjunto de dados em `data` (um array 2D) e `labels` (um array 1D de **inteiros**).
3. Determine a lista de classes representadas no conjunto de dados (deve ser atribuída à variável `classes`).
4. Encontre os valores únicos e suas contagens no conjunto de dados (`data`).
5. Encontre o índice (no array do passo anterior) do valor de medição mais frequente (`most_frequent_index`) e obtenha a própria medição `most_frequent_measurement` usando esse índice.

<div class="hint">Para o último, você poderia usar <code>numpy.argmax</code>.</div>
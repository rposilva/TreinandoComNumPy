## Dividir

Dividir é uma operação inversa a unir. Enquanto unir combina vários arrays em um 
único, dividir separa um array em vários.
As funções do Numpy [`split()`](https://numpy.org/doc/stable/reference/generated/numpy.split.html) e 
[`array_split()`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html) podem fazer isso.
`split()` divide um array em múltiplos sub-arrays de **tamanho igual**. Ela aceita um array e o parâmetro `indices_or_sections`, 
que é um `int` ou um array 1D. Se for um inteiro, `N`, o array será dividido em `N` arrays iguais ao longo do eixo. 
Se tal divisão não for possível, um erro é levantado.
As duas funções que mencionamos são muito semelhantes, a única diferença é que `array_split` permite que o parâmetro `indices_or_sections` 
seja um inteiro que não divide igualmente o eixo. Para um array de comprimento `l` que deve ser dividido em `n` seções, 
ela retorna `l % n` sub-arrays de tamanho `l//n + 1` e o restante de tamanho `l//n`.

```python
x = np.arange(9)
(print(np.split(x, 3)))
```
Saída:
```text
[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
```
Vamos tentar um `N` para o qual o array não pode ser dividido em partes iguais:
```python
x = np.arange(9)
(print(np.split(x, 2)))
```
Saída:
```text
...
ValueError: array split does not result in an equal division
```
No entanto:
```python
print(np.array_split(x, 4))
```
Saída:
```text
[array([0, 1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]
```

Você também pode usar o parâmetro opcional `axis` &mdash; o eixo ao longo do qual 
dividir, o valor padrão é `0`. Ambos os métodos retornam uma lista de sub-arrays que são
visões do original.

Consulte a documentação para mais detalhes sobre esses métodos.

### Tarefa
1. Divida o array `x` em três arrays de formato igual (`arr1`, `arr2` e `arr3`) ao longo do eixo `0`.
2. Divida o array `y` em três arrays `arr4`, `arr5` e `arr6`:
```text
1. [[0 1]
     [4 5]
     [8 9]] 
```
```text
2.  [[ 2]
     [ 6]
     [10]] 
```
```text
3. [[ 3]
     [ 7]
     [11]]
```
<div class="hint">Talvez você queira usar o eixo <code>1</code> no segundo caso.</div>
## Noções básicas de indexação

A indexação de arrays refere-se a qualquer uso de colchetes (`[]`) para indexar valores de arrays.

### Indexação de elemento único

A indexação de elemento único para um array 1D funciona exatamente como em outras sequências padrão do Python. É baseada em zero e aceita índices negativos 
para indexar a partir do final do array.

Ao contrário de listas e tuplas, arrays NumPy suportam indexação multidimensional para arrays multidimensionais. Isso significa que **não é necessário separar 
o índice de cada dimensão em seu próprio conjunto de colchetes**.

```python
x = np.arange(10).reshape(2, 5) # 2-dimensional
print(x[1, 3])
print(x[1, -1])
print(x[0])
```
Saída:
```text
8
9
[0, 1, 2, 3, 4]
```
Note que `x[0, 2]` e `x[0][2]` produzirão o mesmo resultado, `2`. No entanto, o segundo caso é menos eficiente, pois um novo array temporário é criado após o primeiro índice, 
que é subsequentemente indexado por 2.

### Fatiamento

É possível fatiar arrays para extrair arrays com o mesmo número de dimensões, mas de tamanhos diferentes do original. 
O fatiamento funciona exatamente da mesma forma que para listas e tuplas, exceto que pode ser aplicado a múltiplas dimensões também. 
O fatiamento básico ocorre quando obj é um objeto de fatia (construído pela notação `start:stop:step` dentro dos colchetes), um inteiro, 
ou uma tupla de objetos de fatia e inteiros. Todos os arrays gerados pelo fatiamento básico são sempre [visualizações](https://numpy.org/doc/stable/glossary.html#term-view) do array original.

<details>

O fatiamento NumPy cria uma visualização ao invés de uma cópia como no caso de sequências nativas do Python, como string, tupla e lista. 
Deve-se tomar cuidado ao extrair uma pequena porção de um grande array que se torna inútil após a extração, 
pois a pequena porção extraída contém uma referência ao grande array original, cuja memória não será liberada até que todos os arrays derivados 
dele sejam coletados pelo garbage collector. Nesses casos, é recomendado um `copy()` explícito.
</details>

Array 1-D:
```python
x = np.arange(35)
print(x[2:15])
print(x[1:30:5])  # [início:fim:passo]
```
Saída:
```text
[ 2  3  4  5  6  7  8  9 10 11 12 13 14]
[ 1  6 11 16 21 26]
```
Array 2-D:
```python
x = np.arange(35)
y = x.reshape(5, 7)
print(y[1:5:2])
print(y[1:5:2, ::3])  # Primeiramente fatiando na primeira dimensão, depois na segunda.
```
Saída:
```text
[[ 7  8  9 10 11 12 13]
 [21 22 23 24 25 26 27]]
[[ 7 10 13]
 [21 24 27]]
```

Esses exemplos mostram o uso de indexação ao referenciar dados em um array. Eles funcionam tão bem quanto ao atribuir a um array.
Leia mais sobre este tópico [aqui](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing).

### Tarefa
1. Variável `a`: use a indexação no array `x` para extrair o número `19` dele. Por favor, **não** atribua diretamente o valor `19` a `a` :)
2. Variável `b`: use o fatiamento para extrair todos os segundos elementos em todas as segundas linhas (ou seja, elementos com índices começando de `0` com passo `2`). 
O array resultante deve ter forma `(5, 2)`.
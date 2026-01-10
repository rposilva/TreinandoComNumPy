## Criar uma Array

Existem várias maneiras de criar arrays.

Primeiro, você pode criar uma array a partir de uma lista ou tupla regular do Python usando a função `array`.
O tipo da array resultante será deduzido do tipo dos elementos nas sequências de origem.

```python
import numpy as np

a = np.array([0, 1, 2])
b = np.array([0.0, 0.1, 0.2])

print(a.dtype)
print(b.dtype)
```
Saída:
```text
int64
float64
```

`array` transforma sequências de sequências em arrays bidimensionais, sequências de sequências de 
sequências em arrays tridimensionais, e assim por diante.

```python
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
```
Saída:
```text
[[1.5 2.  3. ]
 [4.  5.  6. ]]
```

### Tarefa
Complete a implementação da função `create_array()` para que ela crie uma array a partir de uma lista aninhada
com dimensões especificadas.
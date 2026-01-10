Agora, queremos fazer o mesmo tipo de operação, mas com todas as três cores. Nosso primeiro instinto pode ser repetir a mesma operação que fizemos antes em cada matriz de cores individualmente. No entanto, a radiodifusão do NumPy cuida disso para nós.

Se nossa matriz tiver mais de duas dimensões, então a SVD pode ser aplicada a todos os eixos de uma vez. No entanto, as funções de álgebra linear no NumPy esperam ver uma matriz na forma `(n, M, N)`, onde o primeiro eixo `n` representa o número de matrizes `MxN` na pilha.

No nosso caso, `img_rescaled.shape` é `(408, 612, 3)`, então precisamos permutar os eixos dessa matriz para obter um formato como `(3, 408, 612)`. Felizmente, a função `numpy.transpose` pode fazer isso por nós:

```python
np.transpose(x, axes=(i, j, k))
```
Isso indica que os eixos serão reorganizados de tal forma que a forma final da matriz transposta será reorganizada de acordo com os índices `(i, j, k)`.

Após transpor a matriz, estaremos prontos para aplicar a SVD.

### Tarefa
1. Transpor a matriz `img_rescaled` para que a SVD possa ser aplicada a ela.
2. Aplicar a SVD.

Note as formas de `U`, `s` e `Vt`. Para construir a matriz de aproximação final, precisamos entender como a multiplicação através de diferentes eixos funciona.
## Álgebra linear

Matrizes e operações com matrizes são utilizadas na descrição de muitos algoritmos de aprendizado de máquina devido à eficiência das soluções matriciais em problemas de ML. As funções do NumPy [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html) fornecem implementações eficientes de algoritmos padrão de [álgebra linear](https://en.wikipedia.org/wiki/Linear_algebra): operações com vetores e matrizes. Vetores são arrays 1D do NumPy, enquanto matrizes são arrays 2D e nD.

> <i>A biblioteca SciPy também contém o submódulo [`linalg`](https://docs.scipy.org/doc/scipy/reference/reference/linalg.html#module-scipy.linalg), e há uma sobreposição na funcionalidade. O SciPy contém algumas funções que não são encontradas no `numpy.linalg`, e algumas funções que existem em ambos têm funcionalidades ampliadas no `scipy.linalg`.</i>

### Multiplicação de matrizes

Já vimos que um array pode ser modificado **elemento a elemento** ao adicionar/subtrair ou realizar alguma outra operação com um escalar ou com outro array de mesma forma (ou forma compatível). A multiplicação de matrizes é um procedimento diferente e mais complicado. Ela requer que o número de colunas na primeira matriz (A) seja igual ao número de linhas na segunda matriz (B). Ao realizar a multiplicação de matrizes, estamos calculando o [produto escalar](https://en.wikipedia.org/wiki/Dot_product) entre cada linha na matriz A com cada coluna na matriz B.

<figure>
  <img src="img.png" alt="dot" style="width:300px">
</figure>

Uma das maneiras de calcular o produto de dois arrays usando o NumPy é a função [`numpy.dot(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot). Ela retorna o produto escalar dos arrays `a` e `b`. Se `a` e `b` são ambos escalares ou ambos arrays 1D, então um escalar é retornado; caso contrário, um array é retornado.

```python
a = np.array([[1, 1], [2, 2]])
b = np.array([[0, 10], [0, 10]])
print(np.dot(a, b))
```
Saída:
```text
[[ 0 20]
 [ 0 40]]
```

<details>

Há também a função [`numpy.matmul(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) (atalho: `@`). `matmul` difere de `dot` em dois aspectos importantes:

- Multiplicação por escalares não é permitida.
- Conjuntos de matrizes são transmitidos em conjunto como se as matrizes fossem elementos (os métodos se comportam de maneira diferente quando arrays 3D ou de maior dimensionalidade são passados — veja a documentação dos métodos para mais detalhes).

Para arrays 2D, o comportamento é o mesmo:
```python
a = np.array([[1, 1], [2, 2]])
b = np.array([[0, 10], [0, 10]])
print(a @ b)
```
Saída:
```text
[[ 0 20]
 [ 0 40]]
```
</details>

A multiplicação de matrizes é, sem dúvida, a operação mais importante e amplamente utilizada em aprendizado de máquina. Ela é usada em regressão linear, vários tipos de redes neurais, e outras abordagens.

### Tarefa

Uma simples [rede neural feedforward](https://en.wikipedia.org/wiki/Feedforward_neural_network) consiste em várias camadas de neurônios, cada uma das quais representa uma função que ajusta de alguma forma os valores das características de entrada para produzir o resultado. [Pesos](https://en.wikipedia.org/wiki/Weighting) dos neurônios são os valores usados para modificar os dados de entrada. Os pesos são os parâmetros ajustados durante o procedimento de treinamento e eles afetam o quão bem a rede performa. Uma [função de ativação](https://en.wikipedia.org/wiki/Activation_function) controla a amplitude do resultado: por exemplo, a função [sigmóide](https://en.wikipedia.org/wiki/Logistic_function) usada nesta tarefa produz resultados no intervalo de 0 a 1.

Vamos fingir que já treinamos uma rede neural com 2 camadas e obtivemos os pesos de todos os nós que produzem um resultado decente (`weights_layer1` e `weights_layer2`). Dados de teste (`csv`) são carregados de um arquivo. Divida-os em arrays `values` e classe `labels` (labels estão na última coluna). Em seguida, complete a implementação da função `predict`, que faz o seguinte:
- aceita os dados e os processa na primeira camada: $\sigma(X * W_1)$, onde $X * W_1$ é o produto matricial dos dados de entrada e dos arrays de pesos, e $\sigma$ é a função sigmóide;
- processa o resultado da primeira camada na segunda camada da mesma forma, mas usando o outro conjunto de pesos;
- retorna o resultado em uma forma que pode ser diretamente comparada com as labels reais das classes.

A precisão de suas previsões será impressa se você executar o script.

<div class="hint">Apenas implemente a fórmula dada. A função <code>numpy.dot</code> será útil para ambas as etapas em <code>predict</code>.</div>
<div class="hint">Os dados devem ser processados pela função sigmóide em ambas as etapas.</div>
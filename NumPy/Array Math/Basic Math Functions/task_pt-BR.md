## Funções Matemáticas Básicas

A facilidade de implementar fórmulas matemáticas que funcionam em arrays é uma das razões que torna o NumPy tão amplamente utilizado na comunidade científica do Python.

Por exemplo, esta é a fórmula do [erro quadrático médio](https://en.wikipedia.org/wiki/Mean_squared_error) (uma fórmula central usada em modelos de aprendizado de máquina supervisionado que lidam com regressão):

$$ MeanSquaredError = \frac{1}{n}\sum_{i=1}^{n}(Yprediction_i - Y_i)^2 $$

Implementar esta fórmula em NumPy é simples e direto:

```python
error = (1 / n) * np.sum(np.square(predictions - labels))
```

O que faz com que isto funcione tão bem é que `predictions` e `labels` podem conter um ou mil valores. Eles só precisam ter o mesmo tamanho.

Você pode visualizar desta forma:

![img](img.png)

Neste exemplo, ambos os vetores `predictions` e `labels` contêm três valores, o que significa que `n` possui um valor de três. Após realizarmos as subtrações, os valores no vetor são elevados ao quadrado. Em seguida, o NumPy soma os valores, e o seu resultado é o valor do erro para aquela previsão e a pontuação de qualidade do modelo.

Aqui está uma [lista de funções matemáticas](https://numpy.org/doc/stable/reference/routines.math.html) definidas no módulo NumPy.

### Tarefa

Na teoria da informação, a [entropia](https://en.wikipedia.org/wiki/Entropy_(information_theory)) de uma variável aleatória é o nível médio de "informação", "surpresa" ou "incerteza" inerentes aos possíveis resultados da variável. 
Dada uma variável aleatória discreta $X$ com possíveis resultados $x_{1},...,x_{n}$, que ocorrem com a probabilidade ${P} (x_{1}),...,{P} (x_{n})$, a entropia de $X$ é formalmente definida como:

$$H(X) = - \sum\limits_{i=1}^{n} P(x_i) \log P(x_i)$$

onde $\Sigma$ denota a soma sobre os possíveis valores da variável e a escolha da base do logaritmo varia entre diferentes aplicações. A base 2 fornece a unidade de bits.

Você recebe um conjunto de `probabilidades` de 10 valores diferentes (resultados). Use as [funções matemáticas](https://numpy.org/doc/stable/reference/routines.math.html) do NumPy e a fórmula acima (use a base 2 para o logaritmo) para implementar a função `calculate_entropy`, que deve retornar a entropia dos dados. Não arredonde a resposta.
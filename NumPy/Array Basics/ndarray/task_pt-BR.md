## ndarray

No núcleo do pacote NumPy está o objeto [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) – uma matriz multidimensional homogênea. `ndarray` é uma abreviação de "matriz N-dimensional". Uma matriz N-dimensional é simplesmente uma matriz com qualquer número de dimensões. É uma tabela de elementos (geralmente números), todos do mesmo tipo, indexada por um tupla de inteiros não negativos. No NumPy, as dimensões são chamadas de eixos.

No exemplo abaixo, a matriz `arr` tem 2 eixos. O primeiro eixo tem um comprimento de 2, o segundo tem um comprimento de 3.

```text
[[1., 0., 0.],
 [0., 1., 2.]]
```

Os eixos são numerados a partir de 0. O eixo 0 é uma linha e o eixo 1 é uma coluna. Para acessar os elementos, você deve especificar suas coordenadas ao longo de cada eixo enquanto segue a ordem dos eixos. Por exemplo, para acessar o número `2.` da matriz acima, você deve usar `arr[1, 2]`.

`ndarray` também é conhecido pelo alias `array`. Note que `numpy.array` é diferente da classe `array.array` da Biblioteca Padrão do Python, que só pode manipular matrizes unidimensionais e oferece muito menos funcionalidades. Alguns dos atributos importantes de um objeto `ndarray` são:

- [`ndarray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html) – o número de eixos (dimensões) da matriz.

- [`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html) – as dimensões da matriz: uma tupla de inteiros indicando o tamanho da matriz em cada dimensão. O `shape` de uma matriz com `3` linhas e `5` colunas será `(3, 5)`. O comprimento da tupla `shape` é o número de eixos, `ndim`.

- [`ndarray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html) – o número total de elementos na matriz. Igual ao produto dos elementos de `shape`.

- [`ndarray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html) – um objeto que descreve o tipo dos elementos na matriz. Pode-se criar ou especificar os tipos `dtype` usando tipos padrão do Python. Além disso, o NumPy fornece tipos próprios: `numpy.int32`, `numpy.int16` e `numpy.float64` são alguns exemplos.

Execute o código em `main.py` para ver alguns exemplos na saída. Para executar este script, clique com o botão direito em qualquer lugar na visualização do **Editor** para que você possa ver o menu de contexto e selecione **Executar 'nome_do_script'**. Alternativamente, você pode usar o atalho &shortcut:RunClass; ou o ícone ![](execute.svg) na região de execução.
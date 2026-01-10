Além do NumPy, nesta aula, usaremos outra biblioteca chamada `matplotlib`. Não discutiremos em detalhes aqui, mas haverá um capítulo separado do curso dedicado a esta biblioteca. Por enquanto, se você deseja saber mais sobre ela, consulte a [documentação](https://matplotlib.org/stable/users/index.html). Matplotlib é uma biblioteca amplamente utilizada e abrangente para criar visualizações estáticas, animadas e interativas em Python.

Para transformar sua imagem em um array do NumPy que pode ser manipulado, você pode usar a função `imread` do submódulo `matplotlib.pyplot` (linha 2 no editor de código).

Agora, `img` é um array do NumPy, como podemos ver ao usar a função `type`.

<div class="hint">

Para mais informações sobre como as imagens são tratadas quando convertidas em arrays do NumPy, veja [Um curso rápido sobre NumPy para imagens](https://scikit-image.org/docs/stable/user_guide/numpy_images.html) da documentação do `scikit-image`.
</div>

### Tarefa

- Primeiro, vamos verificar o número de dimensões em nosso array.

- Depois, imprima a forma do array.

Como esta imagem é bidimensional (os pixels na imagem formam um retângulo), poderíamos esperar um array bidimensional para representá-la (uma matriz). No entanto, usar as propriedades `ndim` e `shape` deste array do NumPy nos dá um resultado diferente.

A saída de `shape` é uma tupla com três elementos, o que significa que este é um array tridimensional. De fato, como esta é uma imagem colorida e usamos a função `imread` para lê-la, os dados estão organizados em três arrays 2D representando canais de cor (neste caso, vermelho, verde e azul – RGB). Você pode ver isso olhando para a forma: indica que temos um array de 3 matrizes, cada uma de 408x612.
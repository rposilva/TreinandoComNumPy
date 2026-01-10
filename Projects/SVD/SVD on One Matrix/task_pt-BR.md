Agora, aplicando a função [`linalg.svd`](https://numpy.org/devdocs/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd) à matriz `img_gray`, podemos obter sua decomposição.

### Tarefa

Utilize a decomposição SVD para obter as matrizes ortogonais `U` e `Vt` e a matriz diagonal `s` da matriz `img_gray`. Execute o script para ver se o resultado é o esperado para uma imagem de 408 x 612.

<div class="hint">
Resultado esperado: (408, 408) (408,) (612, 612).
</div>

<div class="hint">
Note que, com uma imagem maior, isso pode demorar um pouco para rodar, dependendo do tamanho da imagem e do seu hardware. Isso é normal! O SVD pode ser um cálculo bastante intensivo.
</div>
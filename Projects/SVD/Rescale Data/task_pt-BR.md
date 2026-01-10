Cada ponto de dados em nosso conjunto de dados atual está no intervalo de `0` a `255`. Como vamos realizar operações de álgebra linear nesses dados, pode ser melhor ter números reais entre `0` e `1` em cada entrada das matrizes para representar os valores RGB.

### Tarefa
Realize uma operação apropriada no array `img` para conseguir um reescalonamento tal que cada ponto de dados seja um número real entre `0` e `1`.

Você pode verificar se o que fez funciona realizando alguns testes. Por exemplo, consultando os valores máximo e mínimo para este array.

<div class="hint">A divisão por um escalar é sua amiga.</div>

<div class="hint">

Você pode usar a função [`numpy.ndarray.max()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html) nos objetos do tipo ndarray sem importar o NumPy.
</div>
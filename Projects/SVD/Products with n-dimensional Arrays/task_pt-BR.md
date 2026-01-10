Se você já trabalhou antes apenas com arrays unidimensionais ou bidimensionais no NumPy, pode ter usado `numpy.dot` e `numpy.matmul` (ou o operador `@`) de forma intercambiável. No entanto, para arrays n-dimensionais, eles funcionam de maneiras muito diferentes. Para mais detalhes, confira a documentação sobre [`numpy.matmul`](https://numpy.org/devdocs/reference/generated/numpy.matmul.html#numpy.matmul).

### Tarefa
Agora, para construir nossa aproximação, precisamos primeiro garantir que nossos valores singulares estejam prontos para a multiplicação, então construímos nossa matriz `Sigma` de forma semelhante ao que fizemos antes. O array `Sigma` deve ter dimensões `(3, 408, 612)`. Para adicionar os valores singulares à diagonal de `Sigma`, aplicaremos novamente a função `fill_diagonal`, usando cada uma das 3 linhas em `s` como a diagonal para cada uma das 3 matrizes em `Sigma`.

Para reconstruir a SVD completa sem aproximação, podemos calcular um produto de `Sigma` e as matrizes ortogonais `U` e `Vt`.

Após rodar o script, observe a forma de `reconstructed`.

A imagem reconstruída deve ser indistinguível da original, exceto por diferenças devido a erros de ponto flutuante da reconstrução. Lembre-se de que nossa imagem original consistia em valores de ponto flutuante no intervalo `[0., 1.]`. A acumulação de erro de ponto flutuante da reconstrução pode resultar em valores ligeiramente fora deste intervalo original (confira a saída da segunda instrução print em `main`). Como `imshow` espera valores dentro do intervalo, podemos usar [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html) para remover o erro de ponto flutuante:

```python
reconstructed = np.clip(reconstructed, 0, 1)
```

Na verdade, `imshow` realiza esse recorte internamente, portanto, se você pular esta linha, poderá ver uma mensagem de aviso dizendo `"Clipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers)."`
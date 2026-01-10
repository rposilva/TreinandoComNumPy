Vamos primeiro ver como o SVD funciona na prática com apenas uma matriz.  
Note que, de acordo com a [colorimetria](https://en.wikipedia.org/wiki/Grayscale#Colorimetric_(perceptual_luminance-reserving)_conversion_to_grayscale), é possível obter uma versão em escala de cinza razoável de nossa imagem colorida se aplicarmos a fórmula:

$$Y = 0.2126R + 0.7152G + 0.0722B$$

onde $Y$ é a matriz representando a imagem resultante em escala de cinza, e $R$, $G$ e $B$ são as matrizes dos canais vermelho, verde e azul que tínhamos originalmente.

### Tarefa

Use a multiplicação de matrizes e a equação acima para obter uma versão em escala de cinza da imagem.  
Execute o script para ver o resultado.

Devemos usar um colormap do `matplotlib` correspondente à cor que desejamos ver em nossa imagem.  
No nosso caso, estamos aproximando a parte em escala de cinza da imagem, então usaremos o colormap `gray`.  
Caso contrário, o matplotlib assumirá um colormap que não corresponde aos dados reais.  
Você pode tentar omitir o argumento `cmap` e ver o que acontece.

<div class="hint">

Note que aqui podemos usar o operador `@`  
(o operador de multiplicação de matrizes para arrays do NumPy, veja [`numpy.matmul`](https://numpy.org/devdocs/reference/generated/numpy.matmul.html#numpy.matmul)).  
</div>
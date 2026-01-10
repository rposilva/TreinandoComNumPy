NumPy refere-se a cada dimensão como um <i>eixo</i>.  
Devido ao funcionamento do `imread`, o primeiro índice no terceiro eixo é o dado do pixel vermelho da nossa imagem.  
O segundo contém o verde e o terceiro – o azul.  
Podemos acessar isso usando a sintaxe de fatiamento.

### Tarefa
Obtenha um array com os dados dos pixels vermelhos fatiando o array original `img`. 

<div class="hint">Você precisa fatiar de forma que preserve tudo nas primeira e segunda  
dimensões e apenas os primeiros elementos na terceira.</div>

Depois, confira o formato do array executando o script.  
Com a saída, podemos ver que cada valor em `red_pixel_data` é um valor inteiro entre  
0 e 255, representando o nível de vermelho em cada pixel correspondente da imagem.  
Como esperado, isto é uma matriz de 408x612.
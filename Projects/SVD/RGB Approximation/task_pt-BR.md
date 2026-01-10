Agora, para realizar a aproximação, devemos escolher apenas os primeiros `k` valores singulares para cada canal de cor.

### Tarefa

Você deve selecionar apenas os primeiros `k` componentes do último eixo para `Sigma` (isso significa que usamos apenas as primeiras `k` colunas de cada uma das três matrizes na pilha) e apenas os primeiros `k` componentes no eixo penúltimo de `Vt` (isso significa que selecionamos apenas as primeiras `k` linhas de cada matriz na pilha `Vt` e todas as colunas).

A forma do array resultante será `(3, 408, 612)` (confira a saída do comando print), que não é a forma certa para mostrar a imagem. Dentro da função `plt.imshow()`, reorganize os eixos de volta para nossa forma original para que você possa ver a aproximação ao executar o script. Esta parte da tarefa não é verificada, mas você provavelmente vai querer completá-la para ver o resultado!

Tente executar isso com diferentes valores de `k`.

Embora a imagem não seja tão nítida, usando apenas um pequeno número de `k` valores singulares (comparado ao conjunto original de 408 valores), podemos recuperar muitas das características distintivas desta imagem.

<div class="hint">Para obter a aproximação, calcule o produto das três matrizes mais uma vez, mas as fatie para manter apenas os componentes de que você precisa.</div>

<div class="hint">A reorganização inicial dos eixos foi feita na linha 9. Você pode usar a mesma operação.</div>

<div class="hint"> 

A solução sugerida usa a sintaxe do [ellipsis](https://numpy.org/devdocs/user/basics.indexing.html#dimensional-indexing-tools). O ellipsis se expande para o número de objetos `:` necessários para a tupla de seleção indexar todas as dimensões.
</div>

## Palavras finais

Claro, este não é o melhor método disponível para aproximar uma imagem. No entanto, de acordo com a álgebra linear, a aproximação que construímos aqui é a melhor que podemos obter para a matriz original em termos da norma da diferença.

Para mais informações, veja <i>G. H. Golub e C. F. Van Loan, Matrix Computations, Baltimore, MD, Johns Hopkins University Press, 1985</i>.

## Qual é o próximo passo?

- Continue explorando o mundo dos Dados com o nosso [Gateway to Pandas](https://plugins.jetbrains.com/plugin/22686-gateway-to-pandas).
- Descubra como construir um labirinto [AMazing](https://plugins.jetbrains.com/plugin/17519-amazing) com Python.
- Aprenda sobre os fundamentos do Aprendizado por Reforço com nosso curso de [Reinforcement Learning](https://plugins.jetbrains.com/plugin/21188-reinforcement-learning-maze-solver).
- Descubra os fundamentos de [Machine Learning](https://plugins.jetbrains.com/plugin/18392-machine-learning-101).
## Introdução

#### Para quem é este tutorial?
Este tutorial é para pessoas que têm um entendimento básico de álgebra linear e arrays no NumPy e desejam descobrir como arrays n-dimensionais (n >= 2) são representados e manipulados. Em particular, se você está curioso para saber como aplicar funções comuns a arrays n-dimensionais (sem usar laços for) ou se quer entender as propriedades de eixo e forma para arrays n-dimensionais, este tutorial pode ser útil.

#### Objetivos de Aprendizagem
Após completar este tutorial, você deve ser capaz de:

- entender a diferença entre arrays unidimensionais, bidimensionais e n-dimensionais no NumPy;

- aplicar algumas operações de álgebra linear a arrays n-dimensionais sem usar laços for;

- entender as propriedades de eixo e forma para arrays n-dimensionais.

#### Conteúdo
A compressão de imagens é algo muito útil porque permite salvar imagens sem ocupar grandes quantidades de memória (aproximação de dados). Nesta lição, usaremos uma [decomposição de matriz](https://en.wikipedia.org/wiki/Matrix_decomposition) da álgebra linear, a decomposição em valores singulares, para gerar uma aproximação comprimida de uma imagem, ainda retendo muitas das características originais.

A lição é baseada no tutorial do NumPy ["Álgebra linear em arrays n-dimensionais"](https://numpy.org/numpy-tutorials/content/tutorial-svd.html).
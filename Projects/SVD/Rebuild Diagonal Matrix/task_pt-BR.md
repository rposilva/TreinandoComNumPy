Note que `s` tem uma forma particular: ela possui apenas uma dimensão. 
Isso significa que algumas funções de álgebra linear que esperam matrizes 2D podem não funcionar aqui. 
Por exemplo, pela teoria, poderia-se esperar que `s` e `Vt` fossem compatíveis para multiplicação. 
Entretanto, isso não é verdade, pois `s` não tem um segundo eixo. Executar `s @ Vt` 
resulta em um `ValueError`. Isso acontece porque ter uma matriz unidimensional para `s` 
neste caso, é muito mais econômico na prática do que construir uma matriz diagonal com os 
mesmos dados.

### Tarefa

Para reconstruir a matriz original, podemos reconstruir a matriz diagonal $\Sigma$ 
com os elementos de `s` em sua diagonal e com as dimensões apropriadas para multiplicação: 
em nosso caso, $\Sigma$ deve ser 408x612, já que `U` é 408x408 e `Vt` é 612x612.

Para adicionar os valores singulares à diagonal de `Sigma`, 
usaremos a função [`fill_diagonal`](https://numpy.org/devdocs/reference/generated/numpy.fill_diagonal.html) do NumPy.

Agora, queremos verificar se o `U @ Sigma @ Vt` reconstruído está próximo da 
matriz original `img_gray`.

O módulo `linalg` inclui uma função [`norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html), que calcula a norma de um vetor ou 
matriz representada em uma matriz NumPy. Por exemplo, a partir da explicação da SVD acima, 
esperaríamos que a norma da diferença entre `img_gray` e o produto SVD reconstruído 
fosse pequena. Depois de rodar o script, você deve ver algo como 
`1.2008248445342685e-12` na segunda linha do seu resultado.
(O resultado real desta operação pode ser diferente dependendo da sua 
arquitetura e configuração de álgebra linear. Mesmo assim, você deve ver um número pequeno.)

Também poderíamos usar a função [`numpy.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html) para garantir que o produto reconstruído 
esteja, de fato, próximo de nossa matriz original (a diferença entre os dois arrays é pequena).
A terceira instrução `print` deve imprimir `True`.
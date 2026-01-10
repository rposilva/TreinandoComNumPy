Para verificar se uma aproximação é razoável, podemos checar os valores em `s` plotando-os. 
```python
plt.plot(s)
plt.show()
```
<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
<img src="s_values.png" alt="s_values" width="400">

No gráfico, podemos ver que, embora tenhamos 408 valores singulares em `s`, a maioria deles (após aproximadamente a 150ª posição) são bem pequenos. Portanto, pode fazer sentido usar apenas as informações relacionadas aos primeiros (digamos, 50) valores singulares para construir uma aproximação mais econômica para nossa imagem.

A ideia é considerar todos os valores singulares em `Sigma`, exceto os `k` primeiros (que são os mesmos que em `s`), como zeros, mantendo `U` e `Vt` intactos, e calcular o produto dessas matrizes como aproximação.

## Tarefa
Construa uma aproximação da imagem calculando o produto das matrizes ortogonais e os primeiros `k = 20` valores singulares da matriz diagonal.
Note que você deve usar apenas as primeiras `k` linhas de `Vt`, já que todas as outras linhas seriam multiplicadas pelos zeros correspondentes aos valores singulares que eliminamos dessa aproximação.
Execute o script para ver o resultado.

Para este exemplo, escolhemos `k = 20`, mas é recomendado que você vá em frente e repita este experimento com outros valores de `k`.  
Cada um dos seus experimentos deve gerar uma imagem ligeiramente melhor (ou pior) dependendo do valor escolhido.

<div class="hint">

Use fatiamento nas matrizes `Sigma` e `Vt`.
</div>

<div class="hint">
A matriz original pode ser reconstruída como um produto das três matrizes obtidas com a SVD.
</div>
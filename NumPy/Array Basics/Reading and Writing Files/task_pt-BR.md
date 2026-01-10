## leitura e escrita de arquivos

Em algum momento, você vai querer salvar seus arrays em disco e carregá-los novamente sem precisar reexecutar o código. Felizmente, há várias maneiras de salvar e carregar objetos com NumPy. Objetos `ndarray` podem ser salvos e carregados a partir de arquivos de disco com as funções [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt) e [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt), que lidam com arquivos de texto normais.

Digamos que você tenha um arquivo 'my_data.csv', que se pareça com isto:
```text
id,value,size,amount
1,0.0660924327,8422,3
2,-0.2533106662,2738,9
3,0.1293063466,2925,10
4,-0.2420789913,1104,1
```
Você pode carregá-lo em um array numpy da seguinte forma:
```python
arr = np.loadtxt('my_data.csv', delimiter=',', skiprows=1)
```
É necessário especificar o delimitador e o número de linhas que precisam ser ignoradas (linhas de cabeçalho).

Se houver valores ausentes em seus dados, use [`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt). Digamos que o conjunto de dados acima tem de fato alguns valores ausentes.
```python
arr = np.genfromtxt('my_data.csv', delimiter=',', skip_header=1)
print(arr)
```
Saída:
```text
[[ 6.60924327e-02  8.42200000e+03  3.00000000e+00]
 [            nan  2.73800000e+03  9.00000000e+00]
 [ 1.29306347e-01  2.92500000e+03  1.00000000e+01]
 [-2.42078991e-01             nan  1.00000000e+00]]
```
### salvando um array em um arquivo de texto

[`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html?highlight=savetxt#numpy.savetxt) irá ajudá-lo com isso. Aqui estão alguns exemplos:
```python
x = y = z = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', x, delimiter=',')    # X é um array
np.savetxt('test.out', (x,y,z))   # x,y,z são arrays 1D de tamanho igual
np.savetxt('test.out', x, fmt='%1.4e')   # usa notação exponencial
```
Saída:
```text
#1:
0.000000000000000000e+00
1.000000000000000000e+00
2.000000000000000000e+00
3.000000000000000000e+00
4.000000000000000000e+00

#2:
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00
0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00

#3:
0.0000e+00
1.0000e+00
2.0000e+00
3.0000e+00
4.0000e+00
```

### tarefa 
Leia os dados do arquivo `somedata.csv` no array `arr`. 
Execute o script para ver os resultados e o arquivo salvo (`test.out`).

<div class="hint">Há valores ausentes nos dados.</div>
<div class="hint">Preste atenção nas linhas extras no topo.</div>
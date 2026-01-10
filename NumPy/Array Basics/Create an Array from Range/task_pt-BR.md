## Criar um Array a partir de um Intervalo

Para criar arrays contendo sequências de números, o NumPy fornece a função [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange). Ela é análoga à função embutida [`range`](https://docs.python.org/3/library/functions.html#func-range) do Python, mas retorna um array.

```python
a = np.arange(10, 100, 10) # 10 é início, 100 é fim, 10 é passo
b = np.arange(0, 5, 0.5)
c = np.arange(10)
print(a)
print(b)
print(c)
```
Saída:
```text
[10 20 30 40 50 60 70 80 90]
[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
[0 1 2 3 4 5 6 7 8 9]
```

Devido à precisão finita de ponto flutuante, geralmente não é possível prever o número de elementos obtidos quando `arange` é usado com argumentos de ponto flutuante. Portanto, na maioria dos casos, é melhor usar a função [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace), que recebe como argumento o número de elementos que desejamos obter em vez do passo:

```python
a = np.linspace(0, 2, 9)                   # 9 números de 0 a 2
print(a)
```
Saída:
```text
[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
```
`linspace` retorna um número especificado de amostras uniformemente espaçadas no intervalo especificado.

### Tarefa
Implemente a função `array_from_range` que retorna um array de inteiros ou floats a partir de um intervalo fornecido. O código no bloco `main` deve ajudá-lo a definir quais parâmetros utilizar.
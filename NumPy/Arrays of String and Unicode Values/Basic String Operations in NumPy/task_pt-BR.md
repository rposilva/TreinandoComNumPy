## Operações Básicas com Strings no NumPy

Há uma série de funções no NumPy que realizam operações com strings em arrays de valores de string e unicode chamando métodos conhecidos de strings Python. Aqui estão alguns exemplos:

- [`numpy.char.lower`](https://numpy.org/doc/stable/reference/generated/numpy.char.lower.html) 
chama [`str.lower`](https://docs.python.org/dev/library/stdtypes.html#str.lower) em cada elemento do 
array de entrada e retorna um array com os elementos convertidos para minúsculas.
- [`numpy.char.capitalize`](https://numpy.org/doc/stable/reference/generated/numpy.char.capitalize.html)
chama [`str.capitalize`](https://docs.python.org/dev/library/stdtypes.html#str.capitalize) e retorna 
uma cópia do array com apenas o primeiro caractere de cada elemento em maiúscula.
- [`numpy.char.startswith(a, prefix)`](https://numpy.org/doc/stable/reference/generated/numpy.char.startswith.html) 
chama [`str.startswith`](https://docs.python.org/dev/library/stdtypes.html#str.startswith) elemento por elemento 
e retorna um array booleano que é `True` quando o elemento string em `a` começa com `prefix`, caso contrário, `False`.
- [`numpy.char.str_len`](https://numpy.org/doc/stable/reference/generated/numpy.char.str_len.html) retorna `len(a)` elemento por elemento, a saída é um array de inteiros.
- [`numpy.char.isnumeric`](https://numpy.org/doc/stable/reference/generated/numpy.char.isnumeric.html) chama a função embutida do Python `isnumeric()` elemento por elemento. Para cada elemento, retorna `True` se houver apenas caracteres numéricos no elemento. A saída é um array com a mesma forma do input.

Você pode explorar mais [operações com strings](https://numpy.org/doc/stable/reference/routines.char.html) disponíveis no módulo NumPy.

### Tarefa

Implemente duas funções:

- `read_data` deve retornar um array com as linhas de texto convertidas para maiúsculas.
- `get_line_lengths` deve retornar um array contendo os comprimentos das linhas de texto de entrada.

<div class="hint">

O oposto de `numpy.char.lower` é [`numpy.char.upper`](https://numpy.org/doc/stable/reference/generated/numpy.char.upper.html).

</div>
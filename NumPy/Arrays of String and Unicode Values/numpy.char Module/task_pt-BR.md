## Módulo `numpy.char`

[`numpy.chararray`](https://numpy.org/doc/stable/reference/generated/numpy.chararray.html) costumava fornecer uma visualização de arrays de valores de string e [unicode](https://docs.python.org/3/howto/unicode.html).
No entanto, a classe `chararray` atualmente só existe para compatibilidade com versões anteriores e não é recomendada para novos desenvolvimentos. A partir do numpy 1.4, se for necessário arrays de strings, é recomendado usar arrays de `dtype` [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_), [`string_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.string_) ou [`unicode_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.unicode_), e utilizar as funções do módulo [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html) para operações vetorizadas rápidas de strings.

### Bytes

Objetos [Bytes](https://docs.python.org/3/library/stdtypes.html#bytes) são sequências imutáveis de bytes únicos. Como muitos protocolos binários principais são baseados na codificação de texto ASCII, objetos bytes oferecem vários métodos que são válidos apenas quando se trabalha com dados compatíveis com ASCII e estão intimamente relacionados a objetos de string de várias outras maneiras. A sintaxe para bytes literais é em grande parte a mesma que para literais de strings, exceto que um prefixo `b` é adicionado:

- Aspas simples: `b'ainda permite "aspas" duplas embutidas'`;

- Aspas duplas: `b'ainda permite aspas simples "embutidas"'`;

- Aspas triplas: `b'''3 aspas simples''', b"""3 aspas duplas"""`.

### `encode` e `decode`

[`numpy.encode`](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html?highlight=encode) chama [`str.encode`](https://docs.python.org/dev/library/stdtypes.html#str.encode) elemento a elemento. Este último retorna uma versão codificada da string como um objeto bytes.

[`numpy.char.decode`](https://numpy.org/doc/stable/reference/generated/numpy.char.decode.html) é usado para
decodificar a string de entrada com base no [codec](https://docs.python.org/dev/library/codecs.html#module-codecs) especificado.
O conjunto de codecs disponíveis é retirado da biblioteca padrão do Python.

```python
x = np.array(['ABCDE', '  fghijklm', 'noPQRST  ', 'UvWxyz'])
print("Input é :", x)
e = np.char.encode(x, encoding='cp500')
print("\nApós codificação: ", e)
d = np.char.decode(e, encoding='cp500')
print("\nApós decodificação: ", d)
```
Saída:
```text
Input é : ['ABCDE' '  fghijklm' 'noPQRST  ' 'UvWxyz']

Após codificação:  [b'\xc1\xc2\xc3\xc4\xc5' b'@@\x86\x87\x88\x89\x91\x92\x93\x94'
 b'\x95\x96\xd7\xd8\xd9\xe2\xe3@@' b'\xe4\xa5\xe6\xa7\xa8\xa9']

Após decodificação:  ['ABCDE' '  fghijklm' 'noPQRST  ' 'UvWxyz']
```

### Tarefa

No momento, a função `read_data` retorna um array de objetos bytes.
Altere o código para que ele retorne um array de strings. A segunda instrução `print` 
deve imprimir `<class 'numpy.str_'>`.
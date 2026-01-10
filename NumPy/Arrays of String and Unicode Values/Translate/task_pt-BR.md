## Traduzir

Às vezes, você pode precisar remover certos caracteres do seu array de strings ou substituí-los por outros caracteres de acordo com alguma regra ou tabela de tradução. Para esse propósito, você pode usar [`numpy.char.translate(a, table, deletechars=None)`](https://numpy.org/doc/stable/reference/generated/numpy.char.translate.html), onde
- `a` é o array de entrada de `str` ou `unicode`;
- `table` é um dicionário ou tabela de mapeamento descrevendo como realizar a substituição;
- `deletechars` (opcional) é uma `str` especificando os caracteres a serem deletados,

Chama [`str.translate`](https://docs.python.org/dev/library/stdtypes.html#str.translate) para cada elemento em `a` e retorna uma cópia da string com todos os caracteres ocorrendo no argumento opcional `deletechars` removidos e os caracteres restantes mapeados através da tabela de tradução fornecida. Ele gera um array de `str` ou `unicode`, dependendo do tipo de entrada.

Você pode usar o método [`str.maketrans()`](https://docs.python.org/dev/library/stdtypes.html#str.maketrans) para criar uma tabela de mapeamento. Se um caractere não for especificado no dicionário/tabela, o caractere não será substituído.

Aqui estão alguns exemplos:

```python
text = np.array(["Hello,", "my", "dear", "friends!"])
print(np.char.translate(text, str.maketrans("aeiouy", "______")))  # Os dois primeiros argumentos de maketrans devem ter comprimento igual.
```
Saída:
```text
['H_ll_,' 'm_' 'd__r' 'fr__nds!']
```
Vamos agora adicionar o parâmetro `deletechars` opcional:
```python
print(np.char.translate(text, str.maketrans("eyn", "EYN", ',!')))
```
Saída:
```text
['HEllo' 'mY' 'dEar' 'friENds']
```
Como você pode ver, no array resultante, não só os caracteres `"eyn"` foram substituídos por `"EYN"`, mas também os caracteres `","` e `"!"` foram deletados.

Você também pode usar [constantes de string](https://docs.python.org/dev/library/string.html?highlight=string%20punctuation#string-constants) no lugar de `deletechars` caso precise se livrar de todos os tipos de pontuação, números ou outros tipos de caracteres. Por exemplo, você pode remover os caracteres `"0123456789"`:

```python
import string

text = np.array(["ABC123,", "Really??!!", "001_So", "Weird!"])
print(np.char.translate(text, str.maketrans("", "", string.digits)))
```
Saída:
```text
['ABC,' 'Really??!!' '_So' 'Weird!']
```
Ou, você pode remover dígitos e pontuação (`string.digits` e `string.punctuation`):
```python
print(np.char.translate(text, str.maketrans("", "", string.digits + string.punctuation)))
```
Saída:
```text
['ABC' 'Really' 'So' 'Weird']
```

### tarefa

Implemente a função `remove_extra_stuff` para que, para o `text` dado, o código imprima `"This is almost a normal sentence now"`.

<div class="hint">Você precisará substituir vogais maiúsculas por minúsculas e remover três tipos diferentes de caracteres.</div>

<div class="hint">Confira a página que descreve constantes de string ligada na descrição da
tarefa para encontrar as que você pode usar.</div>

--------------------------------------------------------------------------------

Parabéns por completar a primeira parte do curso! Agora você pode querer seguir para a próxima seção para testar suas habilidades resolvendo alguns problemas que são mais próximos de aplicações do mundo real.
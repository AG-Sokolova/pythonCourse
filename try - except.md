# Конструкция try - except для обработки исключений

источник: [link](https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html)

источник: [link](https://andreyex.ru/yazyk-programmirovaniya-python/kak-luchshe-vsego-ispolzovat-try-except-v-python-specialno-dlya-nachinayushhix/)



Исключения (exceptions) необходимы для того, что бы сообщить программисту об ошибках.

Причинами ошибок могут быть плохой пользовательский ввод, недостаточные разрешения файла, недоступность сетевого ресурса, недостаточная память или ошибка программиста.

Эти ошибки можно обработать, если в коде использовать обработки исключений и реалиовать их с конструкциями try-except, или tr-except-else, try-except-finally.

------

**Обработать произвольное исключение:**

```python
try:
    #your code
except Exception as ex:
    print(ex)
```

**Поймать несколько исключений в одном блоке Except:**

```python
except (Exception1, Exception2) as e:
    pass
```

**Обработка нескольких исключений с одним блоком Except:**

Способ 1 - требует размещение всех исключений, которые произойдут в виде кортежа.

```python
try:
    file = open('input-file', 'open mode')
except (IOError, EOFError) as e:
    print("Testing multiple exceptions. {}".format(e.args[-1]))
```

Способ 2 - метод обработки каждого исключения в отдельном блоке Except.

```python
try:
    file = open('input-file', 'open mode')
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as e:
    print("Caught the I/O error.")
    raise ex
```

Способ 3 - без упоминания какого - либо атрибута.

```python
try:
    file = open('input-file', 'open mode')
except:
    # В случае каких-либо необработанных ошибок, выбросить
    raise
```

**Повторное повышение исключения в Python**

```python
try:
    # Намеренно вызывать исключение.
    raise Exception('Я учу Python!')
except:
    print("Entered in except.")
    # Re-raise исключение.
    raise
```

**Когда использовать предложение else**

```python
while True:
    # Введите целочисленное значение из консоли.
    x = int(input())
 
    # Разделите 1 на x, чтобы проверить ошибки
    try:
        result = 1 / x
    except:
        print("Случае ошибки")
        exit(0)
    else:
        print("Пример передачи")
        exit(1)
```

**Используйте [Class Finally]**

```python
try:
    # Намеренно вызвать ошибку.
    x = 1 / 0
except:
    # Except clause:
    print("Произошла ошибка")
finally:
    # Finally clause:
    print("Обработан [finally clause]")
```

**Используйте ключевое слово catch, чтобы поймать определенные типы исключений

```python
try:
    # Намеренно вызвать ошибку.
    f = open("no-file")
except IOError as err:
    # Создание экземпляра IOError для бухгалтерского учета.
    print("Ошибка:", err)
    print("Код:", err.errno)
```

**Ручной подъем исключений**

```python
def bad_exception():
    try:
        raise ValueError('Умышленное - не хочу, чтобы это поймали')
        raise Exception('Исключение будет обработано')
    except Exception as error:
        print('Внутри, кроме блока: ' + repr(error))
        
bad_exception()
```

**Как пропустить через ошибку и продолжить выполнение**

Не рекомендуется применять, но бывают исключения.

```python
try:
    assert False
except AssertionError:
    pass
print('Добро пожаловать на andreyex!!!')
```

-----

### Исключения бывают:

- **BaseException** - базовое исключение, от которого берут начало все остальные.
  - **SystemExit** - исключение, порождаемое функцией sys.exit при выходе из программы.
  - **KeyboardInterrupt** - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
  - **GeneratorExit** - порождается при вызове метода close объекта generator.
  - **Exception** - а вот тут уже заканчиваются полностью системные  исключения (которые лучше не трогать) и начинаются обыкновенные, с  которыми можно работать.
    - **StopIteration** - порождается встроенной функцией next, если в итераторе больше нет элементов.
    - **ArithmeticError** - арифметическая ошибка.
      - **FloatingPointError** - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
      - **OverflowError** - возникает, когда результат арифметической  операции слишком велик для представления. Не появляется при обычной  работе с целыми числами (так как python поддерживает длинные числа), но  может возникать в некоторых других случаях.
      - **ZeroDivisionError** - деление на ноль.
    - **AssertionError** - выражение в функции assert ложно.
    - **AttributeError** - объект не имеет данного атрибута (значения или метода).
    - **BufferError** - операция, связанная с буфером, не может быть выполнена.
    - **EOFError** - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
    - **ImportError** - не удалось импортирование модуля или его атрибута.
    - **LookupError** - некорректный индекс или ключ.
      - **IndexError** - индекс не входит в диапазон элементов.
      - **KeyError** - несуществующий ключ (в словаре, множествеили другом объекте). 
    - **MemoryError** - недостаточно памяти.
    - **NameError** - не найдено переменной с таким именем.
      - **UnboundLocalError** - сделана ссылка на локальную переменную в функции, но переменная не определена ранее. 
    - **OSError** - ошибка, связанная с системой.
      - **BlockingIOError**
      - **ChildProcessError** - неудача при операции с дочерним процессом.
      - **ConnectionError** - базовый класс для исключений, связанных с подключениями.
        - **BrokenPipeError**
        - **ConnectionAbortedError**
        - **ConnectionRefusedError**
        - **ConnectionResetError**
      - **FileExistsError** - попытка создания файла или директории, которая уже существует.
      - **FileNotFoundError** - файл или директория не существует.
      - **InterruptedError** - системный вызов прерван входящим сигналом.
      - **IsADirectoryError** - ожидался файл, но это директория.
      - **NotADirectoryError** - ожидалась директория, но это файл.
      - **PermissionError** - не хватает прав доступа.
      - **ProcessLookupError** - указанного процесса не существует.
      - **TimeoutError** - закончилось время ожидания.
    - **ReferenceError** - попытка доступа к атрибуту со слабой ссылкой.
    - **RuntimeError** - возникает, когда исключение не попадает ни под одну из других категорий.
    - **NotImplementedError** - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
    - **SyntaxError** - синтаксическая ошибка.
      - **IndentationError** - неправильные отступы.
        - **TabError** - смешивание в отступах табуляции и пробелов.
    - **SystemError** - внутренняя ошибка.
    - **TypeError** - операция применена к объекту несоответствующего типа.
    - **ValueError** - функция получает аргумент правильного типа, но некорректного значения.
    - **UnicodeError** - ошибка, связанная с кодированием / раскодированием unicode в строках.
      - **UnicodeEncodeError** - исключение, связанное с кодированием unicode.
      - **UnicodeDecodeError** - исключение, связанное с декодированием unicode.
      - **UnicodeTranslateError** - исключение, связанное с переводом unicode.
    - **Warning** - предупреждение

-----

**Примеры наиболее распостраненных ошибок:**

```python
except IOError:
print('Произошла ошибка открытия файла.')
 
except ValueError:
print('Обнаружен не-числовой вход.')
 
except ImportError:
print('Не удалось найти модуль.')
 
except EOFError:
print('Выявлена ошибка EOF.')
 
except KeyboardInterrupt:
print('Неправильный ввод с клавиатуры.')
 
except:
print('Произошла ошибка.')
```

----------

**Простой пример:**

```python
try:
	k = 1 / 0
except ZeroDivisionError:
	print("На ноль делить нельзя")
```
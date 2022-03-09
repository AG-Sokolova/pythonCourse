# Switch-Case в Python

[инструкции Switch-Case в Python](https://nuancesprog.ru/p/12097/)



Встроено только с версии Python 3.10.

Инструкция <code>switch-case</code> в Python  реализована как <code>match-case</code>.

Структурное сопоставление с шаблоном подразумевает определение при операторе `match` искомого значения, после которого можно перечислить несколько потенциальных кейсов, каждый с оператором `case`. В месте обнаружения совпадения между `match` и `case` выполняется соответствующий код.

```
match 'выражение':
    case 'значение':
        #инструкция
    case 'значение':
        #инструкция
    case 'значение':
        #инструкция
    case _:
        #default инструкция
```

**Пример:**

с применением <code>match-case</code>:


```python
http_code = "418"
match http_code:
	case "200":
    	print("OK")
    	do_something_good()
	case "404":
    	print("Not Found")
    	do_something_bad()
	case "418":
    	print("I'm a teapot")
    	make_coffee()
	case _:
    	print("Code not found")
```
с применением <code> if-elif-else </code>:

```python
http_code = "418"
if http_code == "418":
	print("OK")
	do_something_good()
elif http_code == "404":
	print("Not Found")
	do_something_bad()
elif http_code == "418"
	print("I'm a teapot")
	make_coffee()
else:
	print("Code not found") 
```
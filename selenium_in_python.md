# Selenium в Python
https://selenium-python.com/install-geckodriver  
[pypi](https://pypi.org/project/selenium/)  
[geeksforgeeks](https://www.geeksforgeeks.org/find_element_by_class_name-driver-method-selenium-python/)

[Ультимативная шпаргалка по Selenium с Python для автоматизации тестирования](https://habr.com/ru/company/otus/blog/596071/)



**Selenium WebDriver** — это инструмент для автоматизации действий веб-браузера.

В большинстве случаев используется для тестирования Web-приложений, но этим не ограничивается.

#### Установка

1. Необходимо убедиться что установлен pip  `pip3 --version`, если не установлен то устанавливаем через системные настройки
2. Если всё в порядке, то selenium можно установить через pip как обычный пакет `python3 -m pip install selenium`
3. После установки Selenium нообходимо скачать драйвер для браузера. Подробная [инструкция](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/). (для каждого браузера устанавливается свой драйвер)



#### Инициализация дайвера в Python

Импортируем модуль selenium `from selenium import webdriver`

- Chrome

  ```python
  # Initialize Chrome WebDriver
  driver = webdriver.Chrome() 
  ```

- Firefox

  ```python
  # Initialize Firefox/Gecko WebDriver
  driver = webdriver.Firefox()
  ```

- Safari

  ```python
  # Initialize Safari WebDriver
  driver = webdriver.Safari()
  ```

- Internet Explorer

  ```python
  # Initialize IE WebDriver
  driver = webdriver.Ie()
  ```

Если местоположения драйвера браузера нет в переменной PATH (или если его нет в System Path), нужно добавить следующие аргументы:

1. `executable_path`: Путь к вашему веб-драйверу Selenium (бинарный файл)
2. `options`: Параметры, касающиеся выполнения веб-браузеров

**Пример Chrome:**

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(executable_path='путь до драйвера'))
```

**Пример Firefox:**

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(executable_path='./путь до драйвера'))
```



#### Открытие ссылки или документа

Перед выполнением любых операций с веб-элементами, присутствующими на  странице, важно открыть целевой URL-адрес (или тестовый URL-адрес). `driver.get(URL)`

```python
url = "url сайта"
driver.get(url)
```



#### Поиск элементов

Есть много способов искать элементы, но их объединяет необходимость импортировать By 

```
from selenium.webdriver.common.by import By
```

| Метод                                              | Описание                                                     |
| -------------------------------------------------- | ------------------------------------------------------------ |
| find_element(By.ID, "ID элемента")                 | Поиск элемента по атрибуту ID                                |
| find_element(By.CLASS_NAME, "Имя класса")          | Поиск элемента по классу CSS                                 |
| find_element(By.NAME, "Имя")                       | Поиск элемента по имени                                      |
| find_element(By.XPATH, "Путь")                     | Поиск элемента по XPath [руководство по XPath в Selenium](https://www.lambdatest.com/blog/complete-guide-for-using-xpath-in-selenium-with-examples/) |
| find_element(By.TAG_NAME, 'Имя тега')              | Поиск элемента по тегу                                       |
| find_element(By.LINK_TEXT, "Текст ссылки")         | Поиск элемента по тексту ссылки [Локатор текста ссылок в Selenium](https://www.lambdatest.com/blog/using-link-text-and-partial-link-text-in-selenium/) |
| find_element(By.PARTIAL_LINK_TEXT, "Текст ссылки") | Поиск элемента по частичному тексту ссылки [Локатор текста ссылок в Selenium](https://www.lambdatest.com/blog/using-link-text-and-partial-link-text-in-selenium/) |
| find_element(By.CSS_SELECTOR, "Селекторы CSS")     | Поиск по селектору CSS                                       |

#### Обновление страницы

Метод `driver.refresh()` обновляет текущую веб-страницу. Он не принимает никаких аргументов и не возвращает никаких значений.

```python
driver.refresh()
```



#### Ввод текста в веб-элемент

Метод `send_keys()` в Python используется для ввода  текста в текстовый элемент. Такой текст передается методу в качестве  аргумента. 

```python
# get element 
element = driver.find_element(By.ID, "useremail")
  
# send keys 
element.send_keys("emailid@lambdatest.com")
```



#### Удаление текста в веб-элементе

Метод `element.clear()` в Selenium используется для удаления текста из полей, таких как поля ввода формы и т.д.

```python
# get element 
element = driver.find_element(By.ID, "useremail")
  
# send keys 
element.clear()
```



#### Нажатие на веб-элемент

Метод `element.click()` в Selenium используется для нажатия на элемент, такой как ссылка-якорь, кнопка и т.д.

```python
# get element 
button_element = driver.find_element(By.LINK_TEXT, "Start Free Testing")
  
# click the element
button_element.click()
```



#### Перетаскивание веб-элемента

Метод `drag_and_drop(элемент, цель)`в Selenium используется для перетаскивания веб-элементов. (пример приложений Canvas, Google Drive, Trello, Asana и т.д.)

Подробное руководство, в котором есть информация о том, как [выполнять перетаскивание](https://www.lambdatest.com/blog/drag-and-drop-in-selenium-python/) в Selenium.

```python
element = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```



#### Выбор опции

Необходимо импортировать метод

```python
from selenium.webdriver.support.ui import Select
```

`Select`*(элемент)* предоставляет полезные методы для взаимодействия с раскрывающимися списками, выбора элементов и многого другого.

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID, 'city'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

| **Метод**                      | Описание                                                     |
| ------------------------------ | ------------------------------------------------------------ |
| select_by_index(индекс)        | Метод принимает целочисленное значение - индекс опции, которую мы хотим выбрать. |
| select_by_visible_text(“text”) | Метод принимает строковое значение и выбирает опцию, в которой есть нужный текст. |
| select_by_value(значение)      | Метод принимает строковое значение и выбирает параметр с тем же значением атрибута. |
| deselect_all()                 | Метод позволяет отменить выбор всех выбранных опций.         |



#### Навигация между окнами

- **switch_to_window()**

  Метод switch_to_window(“имя_окна”) позволяет переключать на нужное окно.

  ```
  driver.switch_to_window("window_handle")
  ```

- **window_handles** 

  Свойство window_handles  возвращает дескрипторы окон. Теперь метод switch_to_window() можно использовать для перехода к любому окну из списка window_handles. 

  ```python
  for handle in driver.window_handles:
      driver.switch_to_window(handle)
  ```

- **current_window_handle()**

  Метод current_window_handle() возвращает дескриптор текущего окна (или окна в фокусе).

  ```python
  handler = driver.current_window_handle 
  ```



#### Переключение на iFrame

Для того что бы получить доступ к веб-элементам внутри ifFrame необходимо переключиться на ifFrame.

- **switch_to_frame()** 

  Метод switch_to_frame(“имя_iframe”) в Selenium Python позволяет менять  контекст WebDriver из контекста главной страницы. Также мы можем  получить доступ к сабфреймам, добавив между путем и индексом точку.

  ```python
  driver.switch_to_frame("frame_name.0.child")
  ```

- **switch_to_default_content()** 

  Метод switch_to_default_content() позволяет возвращаться обратно к контексту главной страницы.

  ```python
  driver.switch_to_default_content()
  ```

  

#### Обработка всплывающих окон и оповещений

[подробное руководство](https://www.lambdatest.com/blog/selenium-c-tutorial-handling-alert-windows/) 

- **switch_to.alert**

  Свойство switch_to.alert в WebDriver возвращает открытый в данный момент объект alert. Вы можете принять его, отклонить, прочитать содержимое или ввести его в командную строку.

  ```python
  alert_obj = driver.switch_to.alert
  ```

- **alert_obj.accept()**

  После дескриптор окна `alert` (например, `alert_obj`), метод `accept()` поможет принять всплывающее окно предупреждения.

  ```python
  alert_obj = driver.switch_to.alert 
  alert_obj.accept()
  ```

- **alert_obj.dismiss()**

  После переключения на окно `alert` (например, `alert_obj`), можно использовать метод `dismiss()`, чтобы отклонить всплывающее окно предупреждения.

  ```python
  alert_obj = driver.switch_to.alert 
  alert_obj.accept()
  ```

- **alert_obj.text()**

  Этот метод используется для извлечения сообщения из всплывающего окна предупреждения.

  ```python
  alert_obj = driver.switch_to.alert 
  msg = alert_obj.text()
  print(msg)
  ```



#### Получение кода страницы

Метод `page_source()` в Selenium WebDriver используется для получения кода страницы.

```python
page_source = driver.page_source
```



#### Навигация по истории браузера

- **driver.forward()**

  Этот метод позволяет сценариям перемещаться на один шаг вперед по истории браузера.

  ```python
  driver.forward()
  ```

- **driver.back()**

  Этот метод позволяет сценариям перемещаться на один шаг назад по истории браузера.

  ```python
  driver.back()
  ```

  

#### Обработка Cookie в Selenium

- **driver.add_cookie()**

  Этот метод помогает настроить файл cookie для сессии Selenium. Он принимает значения в виде пары ключ-значение.

- **driver.get_cookies()**

  Этот метод выводит все доступные файлы cookie для текущей сессии Selenium.

- **driver.delete_cookie()**

  Есть возможность удалить определенный файл cookie или все файлы cookie, связанные с текущей сессией Selenium.



#### Установка размера окна

Метод `set_window_size()` используется для настройки желаемых размеров окна браузера (ширина и высота).

```python
# Setting the window size to 1200 * 800
driver.set_window_size(1200, 800)
```



#### Создание скриншотов

Метод `save_screenshot()` Selenium WebDriver используется для создания [скриншотов веб-страницы.](https://www.lambdatest.com/blog/python-selenium-screenshots/#Screenshots)

```python
capture_path = 'C:/capture/your_desired_filename.png'
driver.save_screenshot(capture_path)
```


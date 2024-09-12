# python基础

https://github.com/EighteenWu/python_study/blob/main/unit2/%E7%AC%AC%E4%BA%8C%E7%AB%A0%E8%8A%82%E7%AC%94%E8%AE%B0.md  
参考 python基础那一块的知识点~  
常见简单问题:

##### 1、字符串反序输出?

```python
print(str[::-1])


# 第二种方法
def reverse_string(s):
  for i in range(len(s) - 1, -1, -1):
    print(s[i], end='')


# 递归输出
def reverse_string_recursive(s):
  if len(s) == 0:
    return s
  else:
    return reverse_string_recursive(s[1:]) + s[0]
```

##### 2、斐波那契数列求N？

```python
N = int(input("请输入N的值:"))
# 定义一个列表
fib = [0 for x in range(N + 1)]
fib[0] = 0
fib[1] = 1
for i in range(2, N + 1):
  fib[i] = fib[i - 1] + fib[i - 2]
print(fib[N])


# 方法2
def feb(n):
  curr, pred = 0, 1
  k = 0
  while k < n:
    curr, pred = pred, curr + pred
    k += 1
  return curr


print(feb(10))

```

#### 3、判断回文?

```python
str_a = 'abcd'
if str_a == str_a[::-1]:
  print(True)
```

# python进阶

#### ** 用过异常吗？怎么捕获处理异常，其中try，except，else，final怎么用，raise呢？

```python
# python 异常处理基本机制
def find_x(x, adict):
  try:
    # 检查x是否在adict中
    if x in adict:
      print('x存在于adict中')
    else:
      # 如果x不在adict中，抛出一个ValueError异常
      raise ValueError('值不存在')
  except (TypeError, KeyError):
    # 捕获TypeError和KeyError异常
    print("不存在")
  finally:
    print('123456')
```

#### **说说什么是装饰器，你用过哪些装饰器？**

装饰器是一种设计模式，主要用于不修改已有功能的基础上扩展或增强已有功能。它是一种高阶函数，接受一个函数作为入参
并返回一个新的函数;一般情况下用pytest的装饰器比较多，比如@pytest.fixture，@pytest.mark.parametrize,@pytest.skip标记等

```python
# 装饰器示例
# 记录函数运行时间
def run_time(func):
  import time
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f'{func.__name__} run_time: {end_time - start_time}s')
    return result

  return wrapper


@run_time
def sum_a():
  # 计算1-10000000000的和
  sum = 0
  for i in range(10000000):
    sum += i
  print(sum)
```

#### **python内的魔术方法有哪些，简单介绍一下**

python中有很多魔术方法，一般也称为双下划线方法，我知道的有以下几种

* **`__init__`** 构造方法，创建一个类时被调用，用于初始化方法
* **`__new__`** 在实例创建前被调用，用于创建实例，是类级别的方法，创建并返回一个新的对象实例，
* **`__str__`** 显示对象时调用，返回对象的字符串表示
* **`__repr__`** 当使用repr()函数时调用，或者在交互式解释器中显示对象时调用，通常应该返回一个可以用来重建对象的字符串
* **`__len__`** 获取对象长度时调用，返回对象的长度
* **`__getitem__`** 当使用下标访问（如obj[key]）时调用

#### **请问__new__和__init__有什么区别？

`__new__`方法用于创建一个实例，是类级别的方法,方法通常用于控制实例的创建过程，尤其在继承不可变类型(如`int`,`str`,`tuple`)
或者需要自定义实例创建逻辑时

```python
class Test:
  def __new__(cls, *args, **kwargs):
    print('__new__')
    return super().__new__(cls)

  def __init__(self):
    print('__init__')
```

**区别**

* 调用时机
  * `__new__` 在实例创建前被调用
  * `__init__` 在实例创建后被调用，用于初始化实例
* 返回值
  * `__new__` 返回一个新的实例对象
  * `__init__` 不返回任何值，只负责初始化实例
* 参数
  * `__new__`的第一个参数是类本身，后面是传入的参数
  * `__init__`第一个参数是实例本身，表示正在初始化的实例

#### **python中有switch-case模式匹配吗，如果没有，如何实现？**

没有一模一样的语句，但是有math-case语句，需要python版本大于3.10,样例如下

```python
# math-case
def switch_case(x):
  match x:
    case 1:
      print('case 1')
    case 2:
      print('case 2')
    case 3:
      print('case 3')
    case _:
      print('default')
```

使用其他方式实现switch-case，我这边有两个方法

```python
# 实现switch-case 例子1，使用if-else
def switch_case(x):
  if x == 1:
    print('case 1')
  elif x == 2:
    print('case 2')
  elif x == 3:
    print('case 3')
  else:
    print('default')


# 实现swit-case例子2，使用字典映射
def switch_case_2(x):
  cases = {
    1: 'case 1',
    2: 'case 2',
    3: 'case 3',
    'default': 'default'
  }
  print(cases.get(x, cases['default']))
```

#### **列表推导式和字典推导式**
```python
x = [x for x in range(0, 10)]
print(x)

# 字典推导式子1
adict = {k: k ** 2 for k in range(0, 10)}
# 字典推导式子2
fruits = ['apple', 'orange', 'watermelon', 'banana']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)
```
#### **选择排序和冒泡排序**
```python
# 编写一个Python函数，接受一个整数列表作为参数，并返回列表中的最大值。
def bubble_sort(alist):
  for i in range(len(alist)):
    for j in range(len(alist) - i - 1):
      if alist[j] < alist[j + 1]:
        alist[j], alist[j + 1] = alist[j + 1], alist[j]
  return alist


def select_sort(alist):
  for i in range(len(alist)):
    min_index = i
    for j in range(i + 1, len(alist)):
      if alist[min_index] < alist[j]:
        min_index = j
    if min_index != i:
      alist[min_index], alist[i] = alist[i], alist[min_index]
  return alist
```

# pytest

1、pytest运行用例？  
A: pytest -s filename; [显示详细信息]  
2、pytest测试用例格式?  
A: 测试文件以test_*.py或者*_test.py结尾;测试用例以test开头的函数;测试类也是用Test开头的类名;  
3、Fixtures:

* 用于设置测试前的环境或者初始化数据,以及测试后的清理工作;
* 通过装饰器@pytest.fixture来标记，并通过函数参数注入到用例中;

```python
import pytest


@pytest.fixture
def input_value():
  return 38


def test_divisible_by_19(input_value):
  assert input_value % 19 == 0

```

4、参数化测试?  
使用@pytest.mark.parameter装饰器来实现用例参数化；

```python
import pytest


@pytest.mark.parametrize("a, b, expected", [
  (1, 2, 3),
  (4, 5, 9),
  (10, 20, 30)
])
def test_add(a, b, expected):
  assert a + b == expected

```

5、标记(Marking):
使用@pytest.mark装饰器打用例标记;

6、跳过用例:

```python
import pytest


@pytest.mark.skip(reason="跳过原因")
def test_example():
  assert True
```

7、运行特定的测试用例?  
使用命令pytest -k "测试用例名称"

8、pytest-fixture使用夹具:

```python
import pytest


# 定义一个fixture，用于准备测试数据
@pytest.fixture
def data():
  data = [1, 2, 3, 4, 5]
  return data


# 使用fixture进行测试
def test_sum(data):
  result = sum(data)
  assert result == 15
```

9、 说下你们公司的自动化框架的项目结构？

```python
# 业务组件封装
--aw
--payment
payment_commont.py
--c1_task
--account
--finaching
--commmon
db.py
auth.py
--...
# 配置文件
--conf
--sys
payment.yaml
account.yaml
default.yaml
payment.yaml
xxx.yaml
--report
--xxx.html
# 测试案例
--script
--payment
--payment_202_test.py
--payment_202_test.xlsx
--payment_202_test.yaml
--...
test.py
# 工具项
--utils
--gen_case.py
--notify.py
```

# selenium

1、webdriver原理？

* 每个 Selenium 命令，这里指的是所谓的基础操作，例如，点击、输入等，都会创建一条 HTTP 请求，
* 发送给 Browser WebDriver
* Browser WebDriver 使用一个 HTTP Server 监听和接收 HTTP 请求
* HTTP Server 根据协议规则定义这些 Selenium 命令对应的浏览器具体操作
* 浏览器执行这些操作
* 浏览器将执行状态返回给 HTTP Server
* HTTP Server 再将这些状态信息返回给自动化脚本

2、selenium定位方式?

1. id
2. class
3. name
4. 标签
5. css选择器
6. xpath选择器
7. 超链接文本(精准匹配)
8. 超链接文本（模糊匹配）

3、使用优先级  
如果有id优先用id，没有id优先用name属性，在没有的话用css选择器，或者xpath选择器;

4、如果定位不到元素怎么办？
首先看是不是脚本问题，没有加载出来或者遮挡，然后再去看看存不存在dom树上，用css或者xpath绝对路径定位下，实在不行用调用js执行
getElementBy方法定位;

5、显示等待和隐式等待以及固定等待？

```python
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 固定等待
time.sleep(3)

webdriver = webdriver.chrome()

# 显示等待
WebDriverWait(webdriver, 4).until(EC.visibility_of_element_located(locator))

# 隐式等待
webdriver.implicitly_wait(20)

```



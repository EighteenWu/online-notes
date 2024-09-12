# python基础
https://github.com/EighteenWu/python_study/blob/main/unit2/%E7%AC%AC%E4%BA%8C%E7%AB%A0%E8%8A%82%E7%AC%94%E8%AE%B0.md  
 参考 python基础那一块的知识点~  
常见简单问题:
##### 1、字符串反序输出?
```python
print(str[::-1])
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
    k=1
    while k <= n:
    
```

#### 3、判断回文?
```python
str_a = 'abcd'
if str_a == str_a[::-1]:
    print(True)
```


# python进阶


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
--conf 
  --sys
    payment.yaml
    account.yaml
  default.yaml
  payment.yaml
  xxx.yaml
--report
 --xxx.html
--script
 --payment
   --payment_202_test.py
   --..._test.py
--utils
 --gen_case.py
 --notify.py
--
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
#固定等待
time.sleep(3)

webdriver = webdriver.chrome()

#显示等待
WebDriverWait(webdriver,4).until(EC.visibility_of_element_located(locator))

#隐式等待
webdriver.implicitly_wait(20)

```
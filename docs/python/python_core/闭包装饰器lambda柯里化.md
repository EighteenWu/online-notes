# 高阶函数

### return直接返回函数

```python
from math import pi, sqrt


def area(r, shape_constan):
    assert r > 0, "The length cannot be less than 0"
    return r * r * shape_constan


def are_square(r):
    # return r * r
    return area(r, 1)


def area_of_a_circle(r):
    # return r * r * pi
    return area(r, pi)


def area_of_a_hexagon(r):
    # return r * r * 3 * sqrt(3) / 2
    return area(r, 3 * sqrt(3) / 2)


print(area_of_a_circle(3))
print(are_square(3))
print(area_of_a_hexagon(3))
print(are_square(-1))
```

### 函数作为参数进行传递

简单示例1

```python
def add(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def operate(a, b, func):
    return func(a, b)


print(operate(3, 4, add))
print(operate(5, 6, multiplication))
```

简单示例2,CS61A

```python
def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """
    term 入参是cube(k),n是阶数,
    :param n:
    :param term:
    :return:
    """
    total, k = 0, 1
    while k <= n:
        # 这里的tem实际上等同于cube(k)
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    # 版本1
    # total, k = 0, 1
    # while k <= n:
    #     total, k = total + identity, k + 1
    # return total
    # 版本2
    return summation(n, identity)


def sum_cube(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


print(sum_cube(5))
print(sum_naturals(5))
print(summation(5, cube))
```

**将函数作为入参传递给其他函数有几个好处：**

* 灵活性：通过将函数作为参数传递，可以在调用函数时动态地改变函数的行为，实现不同的功能。这种灵活性使代码更加可复用和可扩展。
* 简化代码：使用函数作为参数可以避免重复编写类似的代码逻辑。通过将通用的功能封装在函数中，可以在不同的上下文中重复使用，减少代码量。
* 模块化：函数作为参数的使用可以帮助实现代码的模块化，将不同的功能模块解耦，使代码结构更清晰、易于维护和管理。
* 高阶函数：使用函数作为参数可以实现高阶函数的概念，即函数可以接受函数作为参数或返回函数作为结果。这种功能在函数式编程中非常常见，可以实现更高级的抽象和功能。
* 回调函数：将函数作为参数传递还可以用于实现回调机制，即在某些事件发生或条件满足时调用传入的函数，实现更灵活的控制流程。

### 闭包函数

嵌套函,闭包函数必须调用外部的值，第一次返回函数，第二次返回具体值

```python
def make_adder(n):
    def adder(k):
        return k + n

    return adder


# 第一种调用方式
add_three = make_adder(3)
add_three(4)
print(add_three)  # 返回的是函数adder(k)
print(add_three(4))
# 第二种调用方式
print(make_adder(3)(4))
```

**闭包函数的好处包括：**

* 封装性： 闭包函数可以将一些相关的功能封装在一个函数内部，使得代码更加模块化、可维护性更好。外部函数可以隐藏一些内部实现细节，只暴露需要使用的接口，从而降低了代码的复杂度。
* 状态保持： 闭包函数可以让内部函数访问和修改外部函数的变量，实现状态的保持。这在某些情况下非常有用，比如创建定制的函数或者在需要保持状态的递归函数中。
* 灵活性： 闭包函数可以动态生成函数，根据不同的参数生成不同行为的函数。这种灵活性使得我们可以更容易地实现定制化的功能，降低了重复代码的编写。
* 函数工厂： 闭包函数可以充当函数工厂，根据不同的参数生成不同的函数。这种方式可以简化代码结构，提高代码的可复用性。
* 总的来说，闭包函数可以带来代码的模块化、灵活性和可维护性，同时能够保持状态、封装实现细节，使得代码更加清晰易懂。

#### 装饰器

概念：装饰器是一种涉及模式，可以在不修改原函数的代码情况下实现，动态的给函数或者类添加行为，
装饰器的本质上是一个函数，他接受了一个函数入参，然后返回一个函数入参；新的函数会增强或者修改原有
函数的行为或者功能;  
**用途：**

1. 增强函数行为
2. 代码重用
3. 权限控制

演示例子

```python
# 函数装饰器, 简单实现
def decorator(func):
    def func_name():
        print("该函数的方法名称为:", func.__name__)
        func()

    return func_name


@decorator
def test_add(a, b):
    a, b = b, a


test_add(1, 3)


# 函数装饰器,类
def cls_decator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapper = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapper, name)


@cls_decator
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(f"Value: {self.value}")


# 使用装饰后的类
obj = MyClass("Hello, World!")
obj.print_value()

```

### lambda表达式

概念：lambda表达式是一种匿名函数，没有函数名，这个函数可以接受任意数量的参数

```python
# 简单示例
add = lambda x, y: x + y
print(add(2, 3))
```

1、作为高阶函数的参数，lambda表达式常用于需要函数作为参数的参合  
比如map(),filter(),reduce()等高阶函数

```python
# 使用lambda表达式和map函数对列表中的每个元素进行平方操作
number = [1, 2, 3, 4, 5]
squares = map(lambda x: x * 2, number)
print(list(squares))
```

2、作为函数的返回值

```python
# 根据参数的值返回不同的lambda表达式
def create_lambda(operator):
    if operator == 'add':
        return lambda x, y: x + y
    elif operator == 'subtract':
        return lambda x, y: x - y
    else:
        return lambda x, y: None


add_func = create_lambda('add')
print(add_func(3, 4))  # 输出: 7
```

3、列表排序

```python
# 使用lambda表达式对列表进行排序
items = [('apple', 3), ('banana', 2), ('cherry', 1)]
items.sort(key=lambda item: item[1])
print(items)  # 输出: [('cherry', 1), ('banana', 2), ('apple', 3)]
```

4、列表推导式

```python
# 使用lambda表达式和列表推导式创建一个列表
squares = [(lambda x: x ** 2)(x) for x in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 柯里化函数

概念：将接受多个函数的函数转换接受单入参函数序列,可以理解为创造一个函数模板或者工厂  
**示例**

```python
# 柯里化函数
from operator import add


def curry_2(f):
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


m = curry_2(add)
add_three = m(3)
result = add_three(2)
print(result)


# --> 5


def cube(f):
    def square(x):
        def add(y):
            return x + y
        return add
    return square
```
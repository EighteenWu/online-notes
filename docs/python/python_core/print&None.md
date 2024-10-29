# Python基础知识

## 一、变量与数据类型
### （一）变量
1. **定义**
   - 变量是用于存储数据值的标识符。在Python中，你不需要事先声明变量的类型，直接赋值即可创建变量。
   - 例如：
     ```python
     x = 10
     y = "Hello, World!"
     z = True
     ```
2. **命名规则**
   - 变量名只能包含字母、数字和下划线。
   - 变量名不能以数字开头。
   - 变量名不能是Python中的关键字（如`if`、`else`、`for`等）。
   - 变量名应具有描述性，以便于理解其用途。例如，`age`比`a`更能清楚地表示存储的是年龄信息。

### （二）数据类型
1. **整数（int）**
   - 用于表示整数。例如：`num = 5`。
   - 可以进行加、减、乘、除等数学运算。例如：`result = 3 + 2`，结果为`5`。
2. **浮点数（float）**
   - 用于表示带有小数部分的数字。例如：`pi = 3.14`。
   - 注意：在进行浮点数运算时，可能会出现精度问题。例如：`0.1 + 0.2`的结果可能不是精确的`0.3`，而是近似值`0.30000000000000004`。
3. **字符串（str）**
   - 用单引号（`'`）或双引号（`"`）括起来的字符序列。例如：`name = "John"`。
   - 可以进行字符串拼接。例如：`greeting = "Hello" + " " + "World"`，结果为`"Hello World"`。
   - 可以使用索引访问字符串中的字符。例如：`word = "Python"`，`word[0]`的值为`"P"`。
4. **布尔值（bool）**
   - 只有两个值：`True`和`False`。常用于条件判断。例如：`is_raining = True`。

## 二、输入与输出
### （一）输出
1. **使用`print()`函数**
   - 可以输出各种类型的数据。例如：
     ```python
     print("Hello, World!")
     print(10)
     print(3.14)
     ```
   - 可以同时输出多个值，用逗号分隔。例如：`print("The value of x is", x)`。
2. **格式化输出**
   - 使用`format()`方法进行格式化输出。例如：
     ```python
     name = "Alice"
     age = 25
     print("My name is {} and I am {} years old.".format(name, age))
     ```
   - 也可以使用`f-string`（Python 3.6及以上版本支持）。例如：
     ```python
     name = "Bob"
     age = 30
     print(f"My name is {name} and I am {age} years old.")
     ```

### （二）输入
1. **使用`input()`函数**
   - 用于从用户获取输入。例如：
     ```python
     name = input("Please enter your name: ")
     print("Hello,", name)
     ```
   - `input()`函数返回的是字符串类型。如果需要将输入转换为其他类型，如整数或浮点数，可以使用相应的类型转换函数。例如：
     ```python
     age = int(input("Please enter your age: "))
     price = float(input("Please enter the price: "))
     ```

## 三、运算符
### （一）算术运算符
1. **基本算术运算符**
   - `+`（加法）、`-`（减法）、`*`（乘法）、`/`（除法）、`%`（取模，返回除法的余数）、`**`（幂运算）。例如：
     ```python
     a = 10
     b = 3
     print(a + b)  # 13
     print(a - b)  # 7
     print(a * b)  # 30
     print(a / b)  # 3.3333333333333335
     print(a % b)  # 1
     print(a ** b)  # 1000
     ```
2. **算术运算符的优先级**
   - 幂运算最高，其次是乘、除、取模，加法和减法最低。可以使用括号来改变运算顺序。例如：
     ```python
     result = 2 + 3 * 4
     print(result)  # 14
     result = (2 + 3) * 4
     print(result)  # 20
     ```

### （二）比较运算符
1. **常用比较运算符**
   - `==`（等于）、`!=`（不等于）、`>`（大于）、`<`（小于）、`>=`（大于等于）、`<=`（小于等于）。比较运算符的结果是布尔值。例如：
     ```python
     x = 5
     y = 10
     print(x == y)  # False
     print(x!= y)  # True
     print(x > y)  # False
     print(x < y)  # True
     print(x >= y)  # False
     print(x <= y)  # True
     ```
2. **比较字符串**
   - 字符串按照字典顺序进行比较。例如：
     ```python
     str1 = "apple"
     str2 = "banana"
     print(str1 < str2)  # True
     ```

### （三）逻辑运算符
1. **逻辑与（and）**
   - 当两个条件都为`True`时，结果为`True`，否则为`False`。例如：
     ```python
     age = 20
     is_student = True
     print(age >= 18 and is_student)  # True
     ```
2. **逻辑或（or）**
   - 当两个条件中至少有一个为`True`时，结果为`True`，否则为`False`。例如：
     ```python
     has_license = True
     is_over_18 = False
     print(has_license or is_over_18)  # True
     ```
3. **逻辑非（not）**
   - 对条件取反。例如：
     ```python
     is_raining = True
     print(not is_raining)  # False
     ```

## 四、条件语句
### （一）`if`语句
1. **基本语法**
   - ```python
     if condition:
         # 当条件为True时执行的代码块
     ```
   - 例如：
     ```python
     age = 18
     if age >= 18:
         print("You are an adult.")
     ```
2. **多条件判断**
   - 可以使用`elif`（else if）来进行多个条件的判断。例如：
     ```python
     score = 85
     if score >= 90:
         print("A grade")
     elif score >= 80:
         print("B grade")
     elif score >= 70:
         print("C grade")
     else:
         print("D grade or below")
     ```

### （二）`if`嵌套
1. **语法结构**
   - 可以在`if`语句的代码块中再嵌套`if`语句，用于更复杂的条件判断。例如：
   - ```python
     age = 25
     gender = "male"
     if age >= 18:
         if gender == "male":
             print("Adult male")
         else:
             print("Adult female")
     else:
         print("Not an adult")
     ```

## 五、循环语句
### （一）`for`循环
1. **遍历序列**
   - 可以用于遍历列表、元组、字符串等序列。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     for fruit in fruits:
         print(fruit)
     ```
   - 输出结果为：
     ```
     apple
     banana
     cherry
     ```
2. **使用`range()`函数**
   - `range()`函数可以生成一个整数序列。例如：
     ```python
     for i in range(5):
         print(i)
     ```
   - 输出结果为：
     ```
     0
     1
     2
     3
     4
     ```
   - `range()`函数还可以接受起始值、结束值和步长参数。例如：`range(2, 10, 2)`会生成`2`、`4`、`6`、`8`。

### （二）`while`循环
1. **基本语法**
   - ```python
     while condition:
         # 当条件为True时执行的代码块
     ```
   - 例如：
     ```python
     count = 0
     while count < 5:
         print(count)
         count += 1
     ```
   - 输出结果为：
     ```
     0
     1
     2
     3
     4
     ```
2. **注意事项**
   - 在使用`while`循环时，要确保循环条件最终会变为`False`，否则会导致无限循环。

### （三）循环控制语句
1. **`break`语句**
   - 用于立即跳出循环。例如：
     ```python
     for i in range(10):
         if i == 5:
             break
         print(i)
     ```
   - 输出结果为：
     ```
     0
     1
     2
     3
     4
     ```
2. **`continue`语句**
   - 用于跳过当前循环迭代，直接进入下一次迭代。例如：
     ```python
     for i in range(10):
         if i % 2 == 0:
             continue
         print(i)
     ```
   - 输出结果为：
     ```
     1
     3
     5
     7
     9
     ```

## 六、列表
### （一）定义与初始化
1. **定义列表**
   - 列表是一种有序的可变序列，可以存储不同类型的数据。例如：
     ```python
     numbers = [1, 2, 3, 4, 5]
     fruits = ["apple", "banana", "cherry"]
     mixed_list = [1, "hello", True, 3.14]
     ```
2. **创建空列表**
   - 可以使用空方括号来创建一个空列表。例如：`empty_list = []`。

### （二）列表操作
1. **访问列表元素**
   - 通过索引访问列表中的元素，索引从`0`开始。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     print(fruits[0])  # "apple"
     print(fruits[2])  # "cherry"
     ```
   - 也可以使用负索引从列表末尾访问元素，`-1`表示最后一个元素，`-2`表示倒数第二个元素等。例如：`print(fruits[-1])`会输出`"cherry"`。
2. **修改列表元素**
   - 可以直接通过索引赋值来修改列表中的元素。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     fruits[1] = "orange"
     print(fruits)  # ["apple", "orange", "cherry"]
     ```
3. **添加元素到列表**
   - 使用`append()`方法在列表末尾添加一个元素。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     fruits.append("mango")
     print(fruits)  # ["apple", "banana", "cherry", "mango"]
     ```
   - 使用`insert()`方法在指定位置插入一个元素。例如：`fruits.insert(1, "grape")`，会在索引为`1`的位置插入`"grape"`，列表变为`["apple", "grape", "banana", "cherry", "mango"]`。
4. **删除元素从列表**
   - 使用`remove()`方法删除指定值的元素。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     fruits.remove("banana")
     print(fruits)  # ["apple", "cherry"]
     ```
   - 使用`pop()`方法删除指定索引的元素，并返回该元素的值。如果不指定索引，默认删除最后一个元素。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     removed_fruit = fruits.pop(1)
     print(fruits)  # ["apple", "cherry"]
     print(removed_fruit)  # "banana"
     ```
5. **列表切片**
   - 可以使用切片操作来获取列表的一部分。语法是`list[start:stop:step]`，其中`start`是起始索引（包含），`stop`是结束索引（不包含），`step`是步长（默认为`1`）。例如：
     ```python
     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     print(numbers[2:5])  # [3, 4, 5]
     print(numbers[:5])  # [1, 2, 3, 4, 5]
     print(numbers[5:])  # [6, 7, 8, 9, 10]
     print(numbers[::2])  # [1, 3, 5, 7, 9]
     ```

### （三）列表常用方法
1. **`len()`函数**
   - 用于获取列表的长度，即元素个数。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     print(len(fruits))  # 3
     ```
2. **`sort()`方法**
   - 用于对列表进行排序。默认是升序排序。例如：
     ```python
     numbers = [5, 2, 8, 1, 9]
     numbers.sort()
     print(numbers)  # [1, 2, 5, 8, 9]
     ```
   - 可以通过设置`reverse=True`来进行降序排序。例如：`numbers.sort(reverse=True)`，结果为`[9, 8, 5, 2, 1]`。
3. **`reverse()`方法**
   - 用于将列表中的元素反转。例如：
     ```python
     fruits = ["apple", "banana", "cherry"]
     fruits.reverse()
     print(fruits)  # ["cherry", "banana", "apple"]
     ```

## 七、元组
### （一）定义与初始化
1. **定义元组**
   - 元组是一种有序的不可变序列，可以存储不同类型的数据。例如：
     ```python
     numbers = (1, 2, 3, 4, 5)
     fruits = ("apple", "banana", "cherry")
     mixed_tuple = (1, "hello", True, 3.14)
     ```
2. **创建空元组**
   - 可以使用空圆括号来创建一个空元组。例如：`empty_tuple = ()`。
   - 注意：如果要创建只有一个元素的元组，需要在元素后面加一个逗号。例如：`single_tuple = (1,)`，如果不加逗号，`(1)`会被视为一个整数而不是元组。

### （二）元组操作
1. **访问元组元素**
   - 与列表类似，通过索引访问元组中的元素。例如：
     ```python
     fruits = ("apple", "banana", "cherry")
     print(fruits[0])  # "apple"
     print(fruits[2])  # "cherry"
     ```
   - 也可以使用负索引从元组末尾访问元素。例如：`print(fruits[-1])`会输出`"cherry"`。
2. **元组的不可变性**
   - 元组一旦创建，其元素的值不能被修改。例如，下面的代码会报错：
     ```python
     fruits = ("apple", "banana", "cherry")
     fruits[1] = "orange"  # TypeError: 'tuple' object does not support item assignment
     ```
3. **元组的其他操作**
   - 可以对元组进行一些操作，如连接、重复等。例如：
     ```python
     tuple1 = (1, 2, 3)
     tuple2 = (4, 5, 6)
     concatenated_tuple = tuple1 + tuple2
     print(concatenated_tuple)  # (1, 2, 3, 4, 5, 6)
     repeated_tuple = tuple1 * 3
     print(repeated_tuple)  # (1, 2, 3,
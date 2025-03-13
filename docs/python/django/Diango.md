# Django

Django是一个基于 Python 的 Web 框架，它允许我们编写动态生成 HTML 和 CSS 的 Python 代码。使用像 Django
这样的框架的优点是已经为我们编写了很多可以利用的代码。  
**安装使用:**

* 安装依赖`pip install Django`
* 创建django项目目录`mkdir djangotutorial`
  ,然后切换到对应目录下创建django项目`django-admin startproject mysite djangotutorial`
* 使用命令`python mange.py runsever`，打开初始化django项目
* 创建的项目结构目录如下:

```commandline
djangotutorial/
    manage.py               # 命令行工具
    mysite/                 # 项目实际的python包
        __init__.py         
        settings.py         # Django项目配置文件
        urls.py             # 项目的url声明
        asgi.py             # asgi兼容的web服务器
        wsgi.py             # wsgi兼容的web服务器
```

#### Django项目和应用的区别:

Django项目指的的一个网站使用的配置和应用的集合，项目包括很多个应用;单应用则是某些页面的集合,提供给客户一个功能，单个
应用可以被多个项目所使用;

#### 创建应用:

使用`python manage.py startapp polls`创建一个投票应用;  
目录结构如下:

```commandline
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

创建完成应用程序后，我们需要在项目目录下的`settings.py`文件下的`INSTALLED_APPS`列表，并将新应用程序
的名称添加到此列表中:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'
]
```

#### Routes 路由

1. 为我们的第一个应用`polls`创建一个`Hello, world！页面;在`polls`的`views.py`文件下编写如下代码:

```python
from django.shortcuts import render
from django.http import HttpResponse


# 在此创建视图
def index(request):
    return HttpResponse("Hello, world!")
```

2. 将视图和URL关联起来，每个应用`polls`下面创建`urls.py`文件
3. 在新的py文件下创建可能访问的url模式列表，编写如下代码:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

4. 为整个项目`MyProject`创建`urls.py`文件,并添加所有应用的urls，代码如下所示:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]

```

##### urls 参数化

1. 首先给`views.py`提供一个更加通用的函数:

````python
from django.http import HttpResponse


def greet(request, name):
    return HttpResponse(f'hello, {name}!')
````

2. 在`urls.py`中创建一个更动态路径:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name='brian'),
    path("david", views.david, name='david'),
    path("<str:name>", views.greet, name='greet')
]    
```

##### template 模板

返回自定义的元素样式页面文件:

 ```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
```

上面展示方法太过麻烦，因此一般直接使用如下:

```python
from django.shortcuts import render


def index(request):
    return render(request, "hello/index.html")
```

然后我们可以在对应的应用`polls`下创建`templates/hello`文件夹，在里面新增html文件,至此我们就可以通过i直接访问`hosts/hello`
来查看页面了  
当然初次之外我们还可以使用**Django**的模板语言根据URL来更改访问文件的内容，代码修改如下:

```python
from django.shortcuts import render


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
```

然后我们需要新建一个`greet.html`文件,核心代码如下所示:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>hello</title>
</head>
<body>
<h1>Hello, {{ name }}!</h1>
</body>
</html>
```

在上述代码中，我们使用了`{{context}}`来实现变量传递

##### 动态模板内的Conditionals 条件语句

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Is it New Year's?</title>
</head>
<body>
<body>
{% if newyear %}
<h1>YES</h1>
{% else %}
<h1>NO</h1>
{% endif %}
</body>
</html>
```

##### Styling 样式

如果想给index添加一个样式模板文件,那么则需要在在对应应用下目录`year/static/year/style.css`文件
html文件引入如下所示:

```html
{% load static %}
<DOCTYPE html>
	<html lang="en">
	<link rel="stylesheet" href="{ % static 'newyear/styless.css' %}">
	<head>Test</head>
	<body>
	<h1>
		Test
	</h1>
	</body>
	</html>
```

#### Tasks 任务

##### for循环动态模板语句

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Tasks</title>
</head>
<body>
<ul>
	{% for task in tasks %}
	<li>{{ task }}</li>
	{% endfor %}
</ul>
</body>
</html>
```

##### Forms 表单

使用表单来更新相关页面,首先在`views.py`中新增一个`add`函数

```python
from django.shortcuts import render


def add(request):
    return render(request, 'tasks/add.html')  
```

`url.py`内添加路径:
`path('add', videws.add, name="add")`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Tasks</title>
</head>
<body>
<h1>Add Task:</h1>
<form action="">
	<input type="text" name="task">
	<input type="submit">
</form>
</body>
</html>
```

由于上面的基础部分过多，我们将创建一个基础模板并使用其他模板来继承该基础模板`layout.html`

```html
<!DOCTYPE html>
<html lang="en">
<head><title>
	Tasks
</title>
</head>
<body>
{% block body%}
{% bodyend%}
</body>
</html>
```

在新的`html`文件内继承该模板，示例如下:

```html
 {% extends "tasks:layout.html" %}
{ %  block body %}
<h1>
	Test Extends layout.html
</h1>
{% endblock%}
```

##### html添加变量url

代码如下图所示:

```html
<a href="{% url 'add' %}">Add a New Task<</a>
<a href="{% url 'index' %}">View Tasks</a>
```

因为每个应用内都有`index`的路由，所以我们需要在`urls.py`文件内添加`app_name`应用变量来解决这个问题

```python
from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
```

在用户提交时添加action来发送一个post请求

```html

<form action="{% url 'tasks:add' %}" method="post">
```

##### 防止CSFR跨域攻击

```html

<form action="{% url 'tasks:add' %}" method="post">
	{% csrf_token %}
	<input type="text" name="task">
	<input type="submit">
</form>
```

##### Django Forms Django 表单

使用django自带的表单类操作表单

````python
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Add a new task:
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
````

将操作的数据绑定到表单类中

```python
from django.urls import reverse
from django.http import HttpResponseRedirect


# Add a new task:
def add(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            tasks.append(task)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```

##### session会话

将一些关键性数据存储到request.session中

```python
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
```

## Django Model

**概念:** 模型准确且唯一的描述了数据。每一个模型都映射一张数据库表。  
基础:

* 每个模型都是一个python类,这些类集成`django.db.models.Model`
* 模型类的每个属性都相当于一个数据库的字段
* 利用这些,Django提供了一个自动生成访问数据库的API

### 快速上手

```python
from django.db import models


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

```

我们定义一个Flight模型: 定义了字段目的地，最大长度64，始发地最大长度64，持续时间
上面的每个属性都会被映射成一个数据序列;  
然后我们开始使用命令`python manage.py makemigrations`
来开始迁移生成数据文件,如果未生成则使用`py mange.py makemigarations appname`来生成
接下来使用命令`py manage.py migrate`来开始迁移应用到数据库,迁移完成后可以在当前目录下看到db.sqlite3文件

### Shell壳

如何向数据库添加相关信息，进入到django的sell
`python manage.py shell`

```python
# Import our flight model
from flights.models import Flight

# Create a new flight
f = Flight(origin="New York", destination="London", duration=415)

# Instert that flight into our database
f.save()

# Query for all flights stored in the database
Flight.objects.all()
# Out[4]: < QuerySet[ < Flight: Flightobject(1) >] >

```

因为展示的是对象信息，我们需要重写`Flight`类内的`__str__`方法

```python
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

除此之外，我们不想将名称存存储为每个航班的出发地和目的地，我们需要一个于航班模型相关的
机场模型:

```python
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

在上面的模型中，我们可以看到相关新知识内容:

* 我们指定`orgin`字段和`destination`字段都是外键,意味着它们引用另外一个对象；
* 通过输入`Airport`作为第一个参数，我们指定了该字段引用的对象类型
* 下一个参数`on_delete=models.CASCADE`给出了删除机场后的说明，删除机场后关联的航班也应该对应删除；

需要注意的是,每当我们从`models.py`中进行更改时,我们都必须进行迁移。  
需要注意的是，由于我们在上面的测试内容生成了一个纽约到伦敦的航班,所以我们需要删除条这个数据;  
迁移完成之后,可以尝试在Django Shell中尝试这些新模型:

```commandline
# Import all models
In [1]: from flights.models import *

# Create some new airports
In [2]: jfk = Airport(code="JFK", city="New York")
In [4]: lhr = Airport(code="LHR", city="London")
In [6]: cdg = Airport(code="CDG", city="Paris")
In [9]: nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
In [3]: jfk.save()
In [5]: lhr.save()
In [8]: cdg.save()
In [10]: nrt.save()

# Add a flight and save it to the database
f = Flight(origin=jfk, destination=lhr, duration=414)
f.save()

# Display some info about the flight
In [14]: f
Out[14]: <Flight: 1: New York (JFK) to London (LHR)>
In [15]: f.origin
Out[15]: <Airport: New York (JFK)>

# Using the related name to query by airport of arrival:
In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>
```

import random


def timeer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}的运行时间是{end_time - start_time}s ')
        return result

    return wrapper


@timeer
def select_sort(alist):
    try:
        for i in range(len(alist)):
            min_index = i
            for j in range(i + 1, len(alist)):
                if alist[min_index] > alist[j]:
                    min_index = j
            if min_index != i:
                alist[min_index], alist[i] = alist[i], alist[min_index]
    except IndexError as e:
        print(f'数组越界{e}')
    else:
        print(f'排序完成{alist}')
    finally:
        print('排序结束')


@timeer
def bubble_select(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

    print(alist)


@timeer
def fib(n):
    curr, pred = 0, 1
    while n > 0:
        curr, pred = pred, curr + pred
        n = n - 1
    print(curr)


variables = {}


def variable_decorator(func):
    def wrapper(*args, **kwargs):
        if func.__name__ == 'store_variable':
            variables[args[0]] = args[1]
            return None
        elif func.__name__ == 'read_variable':
            return variables.get(args[0], None)
        else:
            return func(*args, **kwargs)

    return wrapper


@variable_decorator
def store_variable(name, value):
    pass


@variable_decorator
def read_variable(name):
    pass


@variable_decorator
def variable(name):
    pass


store_variable('my_var', 42)
result = read_variable('my_var')
print(result)  # 输出 42
variable(555)

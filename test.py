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


print(bubble_sort([2, 3, 1, 25, 6]))
print(select_sort([2, 3, 1, 25, 6]))


# 编写一个Python函数，接受两个字符串作为参数，检查它们是否是回文字符串，并返回布尔值。
def is_reverse(str1, str2):
    if list(str1)[::-1] == list(str2):
        return True
    else:
        return False


# 编写一个Python程序，实现简单的计算器功能，接受用户输入的两个数字和运算符，然后执行相应的运算。
def caculator(a, c, operator):
    match operator:
        case '+':
            return a + c
        case '-':
            return a - c
        case '*':
            return a * c
        case '//':
            return a // c


# 编写一个Python函数，实现一个简单的日志记录器，能够记录不同级别的日志信息（如INFO, DEBUG, ERROR）。
# 这些题目覆盖了Python的基础语法、数据结构、函数、模块使用以及面向对象编程等知识点，适合有一定经验的测试工程师练习和复习。
def revs(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end="")


# fib求n
def fib(n):
    pred, curr = 0, 1
    k = 0
    while k < n:print(curr)
        curr, pred = pred, pred + curr
        k += 1
        print(curr, end=" ")


fib(10)

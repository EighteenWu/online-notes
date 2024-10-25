```python
print(1, 2, 3)
# 输出1，2，3
print(None)
# 输出None
print(None, None)
# 输出None None
print(print(1), print(2))
# 输出1
# 2
# None None
```

原因是输出返回值的函数将retur n **_None_**  
如果函数没有return返回值，则print语句将会打印出来None值  

###### 课后作业
```python
def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    if x > 0:
        print('positive')
    else:
        print(0)


def x(n):
    while n:
        if n + 6:
            print(n)
        n += 3


if __name__ == '__main__':
    print(how_big(1), how_big(0))
    # python内0是False 1是True，-6+6为0不进入if判断，-3+3为0while循环终止
    x(-12)

'''
第一个输出
postive
0
None None

第二个输出
-12
-9
-3
'''
```
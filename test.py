def reverse_string(s):
    # 从后往前去遍历
    for i in range(len(s) - 1, -1, -1):
        # 打印不会换行
        print(s[i], end='')


def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]


s = input("Enter a string: ")
# reverse_string(s)
# print(reversed(s))


result = reverse_string_recursive(s)
print(result)


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

sum_a()
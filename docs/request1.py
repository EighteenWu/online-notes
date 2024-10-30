def timmer(is_open):
    def decator(func):
        import time
        def wrapper(*args, **kwargs):
            if is_open:
                stat_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f'执行时间{end_time}-{stat_time}s')
            return result

        return wrapper

    return decator


def read_big_files(file_name):
    try:
        with open(file=file_name, mode='rw') as file:
            data = file.read(chunk='20480')
            yield data
    except ValueError as e:
        print('值异常')
    except FileNotFoundError as e:
        print('文件未被找到')
    except FileExistsError as e:
        print('文件关闭失败')
    except BlockingIOError as e:
        print('读取异常')
    else:
        print('读取成功')

    finally:
        file.close()

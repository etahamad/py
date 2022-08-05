from time import time, sleep


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}s to run')
        return result
    return wrapper


@performance
def long_time():
    sleep(2)  # 2 seconds


long_time()

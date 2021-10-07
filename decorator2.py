from time import sleep
import time
import functools


def tired(_func=None, *, seconds=1):
    def slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return slow_down
    else:
        return slow_down(_func)

@tired(seconds=5)
def get_name():
    return "John Doe"


def main():
    print('waiting for output...')
    print(get_name())


if __name__ == '__main__':
    main()

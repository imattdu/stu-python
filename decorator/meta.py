from functools import wraps


def t1(func):
    @wraps(func)
    def t2():
        print(func.__name__)
        print(dir(func))
        func()

    return t2


@t1
def t5():
    print(1111)


if __name__ == '__main__':
    t5()

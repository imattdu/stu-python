def t1(func):
    def wrapper():
        return func()

    return wrapper


@t1
def t2():
    print(123)


# 函数指定参数
def t3(func):
    def wrapper(*args, **kwargs):
        func(args[0])
        return

    return wrapper


@t3
def t4(age):
    print(age, 11)


def t5(age):
    def t51(func):
        def wrapper(*args, **kwargs):
            print('pre', age)
            func(args, kwargs)
            print('end')
            return

        return wrapper

    return t51


@t5(age=11)
def t6(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    t2()
    t4(22)

    t6(1, 2, 3, name=11)

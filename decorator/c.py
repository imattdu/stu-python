class A:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('call')
        self._func()


@A
def t1():
    print('class')


if __name__ == '__main__':
    t1()

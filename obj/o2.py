class P1(object):
    __name = ''
    age = 12

    def __init__(self, _name):
        self.__name = _name

    @classmethod
    def t1(cls):
        print(cls.name)

    @staticmethod
    def t2():
        print('staticmethod')

    @property
    def name(self):
        print(self.__name)

    def __call__(self, *args, **kwargs):
        print(*args)


if __name__ == '__main__':
    # print(P1.t1())
    # print(P1.t2())

    p1 = P1('abc')
    print(p1.name)
    p1.age = 12
    print(p1.__dict__)
    p1.__call__(1, 2, 3)

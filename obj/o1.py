# coding:utf-8

class Person(object):
    name = ''
    __age = 0

    def __init__(self, age):
        print('init')
        self.__age = age


if __name__ == '__main__':
    print(1)
    p1 = Person(11)
    print(p1)

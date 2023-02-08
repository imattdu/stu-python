from functools import cmp_to_key


class User(object):
    def __init__(self, _name, _age):
        self.age = _age
        self.name = _name

    def __str__(self):
        print(self.name, self.age)


# 返回int
def cmp(i, j):
    if i.name == j.name:
        return i.age - j.age
    elif i.name > j.name:
        return 1
    else:
        return -1


def t1():
    us = [User('a', 1), User('b', -99), User('a', 88)]
    r = sorted(us, key=cmp_to_key(cmp))
    for i in r:
        i.__str__()


if __name__ == '__main__':
    l1 = (('zz', 1), ('b', 99), ('c', -3))
    l1 = sorted(l1, reverse=False, key=lambda x: x[1])
    print(l1)
    t1()

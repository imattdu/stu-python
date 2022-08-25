def t1(func):
    def t2():
        func()

    return t2


@t1
def t4():
    print(111)


if __name__ == '__main__':
    t4()

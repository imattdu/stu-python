import threading


class MyThreading(threading.Thread):

    def __init__(self, func, arg):
        super(MyThreading, self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)


def my_func(args):
    print(args)


if __name__ == '__main__':
    obj = MyThreading(my_func, 123)
    obj.start()

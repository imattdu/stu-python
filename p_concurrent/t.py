import threading
import time


class MyThreading(threading.Thread):
    def __init__(self, func, *args):
        super(MyThreading, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args)


def t_f(args):
    if args[1] == 5:
        time.sleep(10)
    # lock.acquire()
    d = args[0]
    d[args[1]] = args[1]
    if args[1] == 30:
        d.clear()
    # lock.release()


if __name__ == '__main__':
    ts = []
    d = {}
    lock = threading.Lock()
    for i in range(100):
        t = MyThreading(t_f, d, i)
        t.start()
        ts.append(t)

    ts.reverse()
    for i in ts:
        i.join()

    print(len(d))
    print(d)

from functools import reduce

if __name__ == '__main__':
    l1 = [1, 2, 3, 99]
    r = reduce(lambda x, y: x + y, l1)
    print(r)

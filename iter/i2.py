class User(object):
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        i = self.a
        i += 1
        if i > 2:
            raise StopIteration
        return i


if __name__ == '__main__':
    u1 = User()
    it = iter(u1)
    print(next(it))
    print(next(it))

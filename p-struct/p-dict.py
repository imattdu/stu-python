if __name__ == '__main__':
    d1 = {1: 2, 2: 3}

    print(d1)
    d1[3] = 3
    print(d1, 'add')
    d1.setdefault(4, 4)
    print(d1, 'setdefault')
    # update
    d1.update({
        2: 2,
        7: 7,
    })

    d1.pop(1)
    del d1[2]
    d1 = {-1: 1, 2: 2}
    d1.popitem()
    d1.clear()

    # print(d1[1])
    print(d1.get(1))

    print(d1, d1.items(), d1.keys(), d1.values())

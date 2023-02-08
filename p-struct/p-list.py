import copy

if __name__ == '__main__':
    l1 = [1, 2, 3]
    # 添加
    print(l1)
    l1.append(9)
    print(l1, 'append')
    l1.insert(0, 9)
    print(l1, 'insert')
    l1.extend([-9, -9])
    print(l1, 'extend')

    l1.remove(9)
    print(l1, 'remove')
    l1.pop(0)
    print(l1, 'pop')
    del l1[0]
    print(l1, 'del')
    l1.clear()
    print(l1, 'clear')

    l1 = [1, 2, 3]
    l1[0] = 99
    print(l1[0], '查看')

    print(len(l1), l1.count(1), 1 in l1)
    # l1.copy copy.deepcopy()
    l2 = l1.copy()
    l3 = copy.deepcopy(l1)
    print(l1, id(l1), l2, id(l2), l3, id(l3), 'copy')

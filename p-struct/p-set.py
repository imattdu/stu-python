if __name__ == '__main__':
    s1 = {1, 2, 3, 3, 3}
    print(s1)
    s1.add(4)
    print(s1, 'add')
    s1.update({2, 3, 4, 5})
    print(s1, 'update')
    s1.remove(3)
    print(s1, 'remove')
    s1.clear()

    s1 = {1, 2, 3, 3, 3}
    s2 = {2, 3}
    print(s1.difference(s2))
    print(s1.union(s2))
    print(s1.isdisjoint(s2))
    print(s1.intersection(s2))

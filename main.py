from functools import cmp_to_key


def cmp(i, j):
    return len(i) - len(j)


if __name__ == '__main__':
    l1 = ['aba', 'ac', 'abdfdfd']
    l1 = sorted(l1, key=cmp_to_key(cmp), reverse=False)
    print(l1)

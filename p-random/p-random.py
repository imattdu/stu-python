import random

if __name__ == '__main__':
    #  不要使用 random 命名
    for i in range(1, 100):
        r = random.randint(1, 10)
        if r == 10:
            print('randint')
            break
    for i in range(1, 100):
        r = random.uniform(0, 1)
        if r == 1:
            print('uniform')

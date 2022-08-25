import random

if __name__ == '__main__':
    cnt = 0
    print(random.uniform(1, 2))
    for i in range(10000):
        if random.randint(1, 100) == 100:
            print(1)
            cnt += 1
    print(cnt)

# [0, 1]
# print(random.random())
#  print(random.randint(1, 100))

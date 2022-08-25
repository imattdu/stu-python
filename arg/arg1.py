import sys

if __name__ == '__main__':
    print(len(sys.argv))
    for idx, i in enumerate(sys.argv):
        print(idx, type(i))

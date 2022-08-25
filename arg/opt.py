import getopt
import sys

if __name__ == '__main__':
    # :该参数有值
    # /Users/matt/.local/share/virtualenvs/stu-python-sIb4ANKk/bin/python
    # /Users/matt/workspace/python/stu-python/arg/opt.py
    # -a 123 -b 12 -c 11 --name=matt
    opts, args = getopt.getopt(sys.argv[1:], '-a:-b:-c:-d', ['name=', 'age'])
    print(opts)

    for k, v in opts:
        print(k, v)

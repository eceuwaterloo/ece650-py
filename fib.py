import sys

def fib(max):
    a, b = 0, 1
    while b < max:
        a, b = b, a+b
    return b

def main():
    print sys.argv
    try:
        umax = sys.argv[1]
        umax = int(umax)
        print 'fib of {0} is'.format(umax), fib(umax)
    except:
        print 'Error: wrong arguments'
        print 'usage: {0} NUM'.format(sys.argv[0])

    return 0

if __name__ == '__main__':
    sys.exit(main())

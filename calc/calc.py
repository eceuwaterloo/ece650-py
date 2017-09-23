import sys

class Register(object):
    def __init__(self):
        self.val = 0

    def add(self, n):
        self.val = self.val + n

    def sub(self, n):
        self.val = self.val - n

    def get(self):
        return self.val

    def reset(self):
        self.val = 0

def parse_line(line):
    sp = line.strip().split()

    if len(sp) > 2:
        raise Exception('Error: too many arguments')
    if len(sp) == 0:
        raise Exception('Error: too few arguments')

    num = None
    if sp[0] == 'c':
        if len(sp) > 1:
            raise Exception("Error: too many arguments for 'c' command")
    elif sp[0] == '=':
        pass
    elif sp[0] == '+':
        num = int(sp[1])
    elif sp[0] == '-':
        num = int(sp[1])
    else:
        raise Exception('Error: unknown command')

    return (sp[0], num)

# YOUR CODE GOES HERE

def main():
    reg = Register()

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break

        try:
            (cmd, num) = parse_line(line)
            if cmd == 'c':
                reg.reset()
            elif cmd == '=':
                sys.stdout.write(str(reg.get()) + '\n')
            elif cmd == '+':
                reg.add (num)
            elif cmd == '-':
                reg.sub (num)
        except Exception as ex:
            sys.stderr.write(str(ex) + '\n')

    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()

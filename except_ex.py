import sys

class ParseException(Exception):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

def parse_line(line):
    if not line.startswith('a'):
        raise ParseException("does not start with 'a'")
    else:
        pass

def run(input, out, err):
    while True:
        line = input.readline()
        if line == '':
            break

        try:
            parse_line(line)
        except ParseException as ex:
            out.write("Error: {0}\n".format(ex))

def main():
    run(sys.stdin, sys.stdout, sys.stderr)

if __name__ == '__main__':
    main()

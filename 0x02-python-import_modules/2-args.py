#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        print('0 arguments.')
    elif ac == 1:
        print('1 arguments.')
        print('1: {}'.format(sys.argv[1]))
    else:
        print('{} arguments.'.format(ac))
        for i in range(1, ac + 1):
            print('{}: {}'.format(i, sys.argv[i]))

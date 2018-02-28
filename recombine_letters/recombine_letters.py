import random


def run(string):
    strspilt = list(string)
    strsize = len(string)
    strnew = []
    lefts = strsize - 1
    for i in range(strsize):
        strnew.append(strspilt.pop(random.randint(0, lefts)))
        lefts -= 1
    recstr = ''.join(strnew)
    return recstr


def run_and_print(string):
    print(run(string))


if __name__ == '__main__':
    teststring = input("input letters:")
    run_and_print(teststring)

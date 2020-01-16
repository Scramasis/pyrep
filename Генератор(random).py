import random
import  math


def masgen(n):
    mlist = [random.randint(1, 10) for i in range(n)]
    print(*mlist)


if __name__ == '__main__':
    masgen(n=12)

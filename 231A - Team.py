if __name__ == '__main__':
    a = input()
    a = int(a)
    n = 0;

    for i in range(0, a):
        sum = 0
        tmp = input()
        for j in range(0, len(tmp)):
            if j % 2 == 0:
                sum = sum + int(tmp[j])
        if sum >= 2:
            n = n + 1
        sum = 0

    print(n)

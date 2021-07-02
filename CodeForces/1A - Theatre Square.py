if __name__ == '__main__':
    n, m, a = input().split()
    m = int(m)
    n = int(n)
    a = int(a)

    width = 0
    height = 0

    if n % a == 0:
        width = int(n / a)
    else:
        width = int(n / a) + 1

    if m % a == 0:
        height = int(m / a)
    else:
        height = int(m / a) + 1

    print(width * height)
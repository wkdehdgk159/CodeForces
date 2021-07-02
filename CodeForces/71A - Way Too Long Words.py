if __name__ == '__main__':
    a = input()
    a = int(a)
    word_list = []

    for i in range(0, a):
        tmp = input()
        if len(tmp) <= 10:
            print(tmp)
        else:
            print(tmp[0] + str(len(tmp)-2) + tmp[-1])

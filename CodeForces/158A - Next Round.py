if __name__ == '__main__':
    m, k = input().split()
    m = int(m)
    k = int(k)

    # 띄어쓰기된 원소들을 int 그리고 list 형태로 저
    score_list = list(map(int, input().split()))

    cutline = 0
    count = 0장

    for i in range(0, m):
        if i == k - 1:
            cutline = score_list[i]

    for i in score_list:
        if i >= cutline and i > 0:
            count = count + 1;

    print(count)
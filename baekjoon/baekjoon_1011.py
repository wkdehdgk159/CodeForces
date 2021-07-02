import math

max_len = math.pow(2, 31)

active_per_dist = [0]
index = 0;
value = 0;

while True:
    value += 1

    index += 1
    active_per_dist.append(active_per_dist[index - 1] + value)
    index += 1
    active_per_dist.append(active_per_dist[index - 1] + value)

    if active_per_dist[index] > max_len:
        break

iteration = int(input())

for i in range(iteration):
    x, y = input().split()
    x = int(x)
    y = int(y)
    diff = y - x
    for j in range(len(active_per_dist)):
        if active_per_dist[j - 1] < diff and active_per_dist[j] >= diff:
            print(j)
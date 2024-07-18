# n 바구니 개수 , m 줄
n, m =map(int,input().split())
n_list = [0] * (n + 1)
for i in range(m):
    x, y, i = map(int,input().split())
    for j in range(x, y + 1):
        n_list[j] = i

for i in range(1, len(n_list)):
    print(n_list[i], end=" ")
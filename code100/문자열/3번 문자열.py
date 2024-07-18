n = int(input())
msg = ""
for index in range(n):
    a = list(input())
    msg = a[0] + a[-1]
    print(msg)
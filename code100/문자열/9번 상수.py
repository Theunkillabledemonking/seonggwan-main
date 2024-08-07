# # 상수!
# # 입력 받는다
# a = input().split()
# new = []
# for i in a:
#     new.append(i[: :-1])

# # 입력받은 두수중에 가장 큰 값을 리버스해서 출력시킨다.
# print(max(new))

a,b = input().split()
a = int(a[: : -1])
b = int(b[: : -1])

print(a) if a > b else print(b)


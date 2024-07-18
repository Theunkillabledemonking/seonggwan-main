# 과제 28명 제출 남은 오름차순으로 출력
grad_list = [i for i in range(1, 31)]
for i in range(28):
    n = int(input())
    grad_list.remove(n)

for i in grad_list:
    print(i)
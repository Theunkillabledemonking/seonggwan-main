# 코딩은 체육과목 두둥!

# 입력한 4의 배수마다 'long' //4+ 'int'출력

n = int(input())
answer = 'int'

for i in range(n//4):
    answer = 'long ' + answer
    
print(answer)
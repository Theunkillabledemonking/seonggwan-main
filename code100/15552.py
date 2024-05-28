# 조건 반복문 

# 첫 줄에는 테스트케이스의 갯수 입력
import sys

inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
# 각각 맞는 합에 더해서 출력

# sys.stdin(표준입력), sys.stdou(출력), sys.stderr(오류 스트림제어)

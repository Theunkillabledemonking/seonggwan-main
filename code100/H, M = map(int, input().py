# # 시작하는 시각과 오븐구이를 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각 계산

# # 첫재 줄에는 현재시각, 두번째 줄에는 필요한 시간 분 단위

# #출력 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력

# h, m = map(int,input().split())
# cook = int(input())

# h += cook // 60
# m += cook % 60

# if m >=60 :
#     m -= 60
#     h += 1
    
    
# if h >= 24:
#     h -= 24
    
# print(h,m)






# 시각과 분을 입력하는 문구 출력
h, m = map(int,input().split())
# 요리하는데 걸리는 시각을 출력.0
c = int(input())
# 시각을 설정
h += c // 60
# 분을 설정
m += c % 60

if m >= 60:
    m -= 60
    h += 1

if h >= 24 :
    h -= 24 
    
print (h,m)
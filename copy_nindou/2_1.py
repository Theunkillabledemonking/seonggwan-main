mt2 = int(input("토지의 면적을 제곱미터(m2) 단위로 입력하세오:"))
while not mt2 >= 0:
    mt2 = int(input("잘못된 입력입니다. \n 다시 토지의 면적을 제곱미터(m2) 단위로 입력하세요"))

m_ft = mt2 * 10.7639
m_ac = mt2 / 4046.86

print(f"{mt2} 제곱미터는 {m_ft} 평방피트입니다.")
print(f"{mt2} 제곱미터는 {m_ac} 에이커입니다.")
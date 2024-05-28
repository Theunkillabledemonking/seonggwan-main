
def stock_trading_simulation(initial_capital,stock_purchase_price,the_number_of_shares,selling_price):
    # 주식 구매 비용 계산 : 구매 가격과 주식 수를 곱하여 총 구매 비용 계산
    purchase_cost = stock_purchase_price * the_number_of_shares
    # 남은 자본금 계산 : 초기 자본금에서 총 구매 비용을 빼서, 주식 구매 후 남은 자본금을 계한
    remaining_capital = initial_capital - purchase_cost
    # 판매 예상 이익 계산 : 판매할 때의 주식 가격과 주식 수를 곱하여 총 판매를 금액을 계산
    the_amount_of_sales = selling_price * the_number_of_shares
    anticipated = the_amount_of_sales - purchase_cost   #예상 이익 or 손실
    
    # 이익이면 이익이라고 손실이라면손실 출력, 
    print (f"구매 후 남은 자본금 :{remaining_capital:.2f}")
    if anticipated > 0:
        print(f"예상 이익 : {anticipated:.2f}")
        print("예상되는 이익입니다.")
    else :
        print(f"예상 이익: {anticipated:.2f}")
        print("예상되는 손실입니다.")
        
    return remaining_capital, anticipated

# 여기서 총 구매 비용을 빼서 예상 이익 또는 손실 계산

# 입력값 넣기
initial_capital = float(input("초기 자본금을 입력하세요: "))
stock_purchase_price = float(input("주식 가격을 입력하세요: "))
the_number_of_shares = float(input("구매할 주식 수를 입력하세요: "))
selling_price = float(input("판매할 때의 주식 가격을 입력하세요: "))
# 결과 출력 구매후 남은 자본금과 예상 이익(또는 손실)을 출력

remaning_capital, anticipated = stock_trading_simulation(initial_capital,stock_purchase_price,the_number_of_shares,selling_price)

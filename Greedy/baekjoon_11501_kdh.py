# 11501 주식
from collections import defaultdict
T=int(input())
for _ in range(T):
    days=int(input())
    price_list=list(map(int,input().split()))
    sorted_price_list=sorted(price_list,reverse=True)
    remain_prices=defaultdict(int)
    for price in sorted_price_list:
        remain_prices[price]+=1

    stock_amount=0
    result_money=0
    
    for day_price in price_list:
        if day_price!=next(iter(remain_prices)): # 알고있는 최고가 보다 현재 가격이 낮을때,
            stock_amount+=1
            result_money-=day_price # 주식 1개 삼
        else:
            result_money+=stock_amount*day_price # 가진 주식 다 팔기
            stock_amount=0
        
        remain_prices[day_price]-=1
        if remain_prices[day_price]==0: # 오늘 가격을 reamin_prices에서 1감소 
            del remain_prices[day_price] # 0이면 해당 가격은 앞으로 안나옴

    print(result_money)
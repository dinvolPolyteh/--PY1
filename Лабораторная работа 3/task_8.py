money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05




def live_exp(money_capital,salary,spend,increase = 0.05):
    month = 0
    while True:
        money_capital -= spend
        if money_capital <=0:
            break
        spend = spend*(1+increase)
        month +=1
        money_capital+=salary

    return month

month = live_exp(money_capital,salary,spend)  # количество месяцев, которое можно прожить


# TODO Оформить решение

print(month)

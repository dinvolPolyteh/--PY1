salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def need_money(salary,spend,months,increase = 0.03):
    #money = -months*salary + spend*(1-(1+increase)**months)/(1-(1+increase))
    money = 0
    for i in range(0,months):
        money += spend - salary
        spend *= (1+increase)
    return money
print(round(need_money(salary,spend,months)))

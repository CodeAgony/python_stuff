def calc_salary(rub, uah_exchange):
    min_wage = 3300
    rub2uah = rub*uah_exchange
    times = rub2uah/(min_wage/2)
    print ("Your pay for these 2 weeks is {:.2f}, {:.2f} times higher than the minimum wage".format(rub2uah, times))


calc_salary(18610, 0.39)
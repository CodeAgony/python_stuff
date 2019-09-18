import random
# Generates 6 random numbers from 1 to 59 and 1 from 1 to 35 and prints them out in a string
def powerball():
    num1 = str(random.randrange(1, 60))
    num2 = str(random.randrange(1, 60))
    num3 = str(random.randrange(1, 60))
    num4 = str(random.randrange(1, 60))
    num5 = str(random.randrange(1, 60))
    num6 = str(random.randrange(1, 60))
    jackpot = str(random.randrange(1, 36))
    print ("Today’s numbers are {}, {}, {}, {}, and {}.The Powerball number is {}.".format(num1, num2, num3, num4, num5, num6, jackpot))

powerball()
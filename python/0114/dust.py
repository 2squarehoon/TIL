dust = 120

def dust_quantity(dust):
    if dust > 150:
        print('매우 나쁨')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    else:
        print('좋음')

dust_quantity(100)
dust_quantity(20)
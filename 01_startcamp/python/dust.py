# ctrl + n => ctrl + s => dust.py
def dust_quality(dust):
    if dust > 150:
        print('매우 나쁨')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    else:
        print('좋음') 
        print('여행가자~!')

dust_quality(100)
dust_quality(30)
dust_quality(600)
# 로또를 n장 사고싶다.
import random

def lotto_maker(n):
    for i in range(n):
        print(sorted(random.sample(range(1, 46), 6)))

lotto_maker(3)
# 로또 5장 사겠다
import random

for i in range(5):
    print(sorted(random.sample(range(1, 46), 6)))
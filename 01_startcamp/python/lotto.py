# 1. random 모듈 불러오기
import random
# 2. 숫자 통 (1~45)
numbers = range(1, 46)  # range(n, m) : n이상 m미만 
# 3. 숫자 통에서 6개를 sample
# random.sample(통, 개수)
# 4. 결과 출력
for i in range(5):
    lotto_number = random.sample(numbers, 6)
    print(sorted(lotto_number))

# 1. 모듈 불러오기
import random

# 2. 숫자 통(1~45) 
# 짤팁 : 변수설정할때 여러개가 포함된 리스트면 복수형(~s)를 붙여라
# range(n, m) : n이상 m미만
numbers = range(1, 46)

# 3. 그 중에서 6개를 sample(통, 개수)
my_pick = random.sample(numbers, 6)

# 4. 그 결과를 출력
# print(sorted(my_pick))
# print(sorted(random.sample(numbers, 6)))

# 한줄짜리 코드로 요약
# print(sorted(random.sample(range(1, 46), 6)))

# 5장 사겠다
for i in range(5):
    print(sorted(random.sample(range(1, 46), 6)))
# 1. 모듈 불러오기(파이썬 내장함수)
import random

# 2. 점심 메뉴 리스트 만들기
lunch_box = ['Jjajangmyeon', 'Hamburger', 'Gukbab', 'Ramen', 'Jeyukdeopbab', 'Yangnyeomchicken']
dinner_box = ['Maekju', 'Soju', 'Wine', 'Cocktail']

# 3. 하나를 랜덤으로 선택하여 저장 
today_menu = random.choice(lunch_box)

# 4. 저장한 것을 출력
print(today_menu)
print(random.choice(dinner_box))

# print(lunch_box)
# print(lunch_box[3])



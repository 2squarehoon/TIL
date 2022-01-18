greeting = 'Guten Tag!!!!!'

# while문? 
# 10번 실행하고 싶어. 
# 0부터 9까지 올라가면서 10되면 종료하도록?
i = 0 
while i < 10: # 해당 조건이 False가 되면, 종료!
    print(greeting)
    i = i + 1

# for문? 
# 10번 실행하고 싶어.
# 통 : range(10)
print(range(10))

for i in range(10):
    # i = _________
    print(i)

lunch_box = ["kfc", "버거킹", "맥도날드"]
# 런치박스의 내용을 하나씩 menu에 넣어줌.
for menu in lunch_box:
    # menu = 
    print(menu)

# 런치박스의 길이(len) 만큼 숫자들을 나열시키고 (range)
# 하나씩 i에 인덱스를 넣어줌
for i in range(len(lunch_box)):
    # 인덱스에 하나씩 접근
    print(lunch_box[i])
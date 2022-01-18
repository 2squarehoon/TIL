# Daily Homework

## Python 02. 데이터 & 제어문

### 1. Mutable & Immutable

``` python
mutable_container = ['list', 'set', 'Dictionary']
immutable_container = ['String', 'tuple', 'range']
```

### 2. 홀수만 담기

``` python
odd_num = list(range(51)[1::2])
```

### 3. Dictionary 만들기

``` python
dict_members = {'고형주':'31', '곽종환':'27', '김도현':'27', '김미애':'26', '김준우':'26', '김찬영':'28', '김혜린':'25', '류현수':'27', '민경욱':'27', '박현진':'27', '신선영':'25', '엄윤규':'30', '유지언':'29', '유현욱':'28', '윤신희':'28', '윤현식':'28', '이동환':'27', '이승훈':'29', '임완택':'27', '전민재':'28', '정예원':'24', '정의찬':'30', '정지은':'25', '채송지':'27', '한상우':'26', '한하평':'29', '호인영':'27'}
```

### 4. 반복문으로 네모 출력

``` python
n = 5
m = 9

for i in range(m):
    print('*' * n)
```

### 5. 조건 표현식

``` python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```

### 6. 평균 구하기

``` python
scores = [80, 89, 99, 83]
total_num = 0
for n in scores:
    total_num += n
avr_num = total_num / len(scores)
print(avr_num)
    
```



# Daily Workshop

## Python 02. 데이터 & 제어문

### 1. 간단한 N의 약수

``` python
N = int(input('N을 입력하시오.(단, N은 1이상 1000이하의 정수이다.) : '))
if N <= 0 or N > 1000:
    print('1이상 1000이하의 정수만 입력하시오.')
else:
    for n in range(N+1)[1::]:
        if N % n == 0:
            print(n, end = ' ')
```

### 2. 중간값 찾기

``` python
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]


```

### 3. 계단 만들기

``` python

```


# Daily Homework

## Python 03. 함수

### 1. Built-in 함수

``` python
print()
int()
float()
str()
set()
dict()
list()
# ...etc
```

### 2. 정중앙 문자

``` python
def get_middle_char(chars):
    if len(chars) % 2:
        return chars[(len(chars) // 2):-(len(chars) // 2):]
    else:
        return chars[((len(chars) // 2)-1):(-(len(chars) // 2)+1):]

```

### 3. 위치 인자와 키워드 인자

``` python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
ssafy('허준')
ssafy(location='대전', name='철수')
ssafy('영희', location='광주')
ssafy(name='길동', '구미') -> 오류 발생, 키워드를 설정하면 이후 순서는 박살난다. 
```

### 4. 나의 반환값은

``` python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
답 : None
```

### 5. 가변 인자 리스트

``` python
def my_avg(*numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

my_avg(77, 83, 95, 80, 70)
```

### 

# Daily Workshop

## Python 03. 함수

### 1. List의 합 구하기

``` python
def list_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total
    
    
list_sum([1, 2, 3, 4, 5])
```

### 2. Dictionary로 이루어진 List의 합 구하기

``` python
def dict_list_sum(students):
    result = 0
    for i in range(len(students)):
        result += students[i]['age']
    return result
```

### 3. 2차원 List의 전체 합 구하기

``` python
def all_list_sum(args):
    total = 0
    for i in range(len(args)):
        for j in range(len(args[i])):
            total += args[i][j]
    return total

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
```


# Daily Homework

## Python 04. 함수

### 1. 이름 공간(Namespace)

``` python
Local scope : 함수
Enclosed scope : 특정 함수의 상위 함수
Global scope : 함수 밖의 변수 혹은 import된 모듈
Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
```

### 2. 매개변수와 인자, 그리고 반환

``` python
답 : (1), tuple 형태로 반환한다. (a, b)
```

### 3. 재귀 함수

``` python
재귀 호출을 사용함으로써 변수 사용을 줄일 수 있다. 
```



# Daily workshop

## Python 04. 함수

### 1. 숫자의 의미

``` python
def get_secret_word(numbers):
    word = ''
    for i in range(len(numbers)):
        word += chr(numbers[i])
    return word
get_secret_word([83, 115, 65, 102, 89])
```

### 2. 내 이름은 몇일까?

``` python
def get_secret_number(words):
    sum = 0
    for i in range(len(words)):
        sum += ord(words[i])
    return sum
get_secret_number('tom')
```

### 3. 강한 이름

``` python
def get_strong_word(word1, word2):
    sum1 = 0
    sum2 = 0
    for i in range(len(word1)):
        sum1 += ord(word1[i])
    for j in range(len(word2)):
        sum2 += ord(word2[j])
    if sum1 >= sum2:
        return word1
    else:
        return word2
    
get_strong_word('z', 'a')
get_strong_word('tom', 'john')
```


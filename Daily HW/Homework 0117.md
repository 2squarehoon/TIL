# Daily Homework

## Python 01. 데이터 & 제어문

### 1. Python 예약어

```python
import keyword
print(keyword.kwlist)
```

``` Answer
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 2. 실수 비교

``` python
num1 = 0.1 * 3
num2 = 0.3
# 1
abs(num1 - num2) <= 1e-10

# 2
import sys
abs(num1 - num2) <= sys.float_info.epsilon

# 3
import math
math.isclose(num1, num2)
```

### 3. 이스케이프 시퀀스

``` python
# (1)
\n

# (2)
\t

# (3)
\\
```

### 4. String Interpolation

``` python
name = '철수'
print('안녕, %s야' % name)
print('안녕, {}야'.format(name))
print(f"'안녕, {name}야'")
```

### 5. 형 변환

``` python
str(1)
int('30')
int(5)
bool('50')
int('3.5') #오류 발생, integer는 정수값인데 3.5인 실수가 있어서 ValueError 발생
```

### 6. 네모 출력

``` python
n = 5
m = 9
line = '*' * n
print('%s\n' %line*m)

# or
print(('*' * n + '\n') * m) # 더하기를 붙이자
```

### 7. 이스케이프 시퀀스 응용

``` python
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

### 8. 근의 공식

``` python
a = float(input('a값을 입력하세요. : '))
b = float(input('b값을 입력하세요. : '))
c = float(input('c값을 입력하세요. : '))

root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a) 
root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
print(root1, root2)
```



# Daily Workshop

## Python 01. 데이터 & 제어문

### 1. 세로로 출력하기

``` python
number = int(input('자연수 n을 입력하시오. : '))

for i in range(number):
    print(i+1)
```

### 2. 거꾸로 세로로 출력하기

``` python
number = int(input('자연수 n을 입력하시오. : '))

for i in range(number+1):
    print(number-i)
```

### 3. N줄 덧셈

``` python
number = int(input('자연수 n을 입력하시오. : '))
total_num = 0
for i in range(number):
    total_num += i+1
    
print(total_num)
```
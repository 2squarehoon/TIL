"""
12221: 구구단2
"""

T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    if A >= 10 or B >= 10:
        answer = -1
    else:
        answer = A*B
    print(f'#{test_case} {answer}')
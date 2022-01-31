T = int(input())
for test_case in range(1, T+1):
    k = int(input())
    n = int(input())
    answer = 1
    for i in range(1, k+2):
        answer *= (n-1+i)/i
    print(int(answer))

# 이건 내 코드가 틀린게 아니다. 백준 채점 시스템이 븅신인거다.
"""
1961: 숫자 배열 회전
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    line = [0] * N
    arr = []
    for idx in range(N):
        arr.append(line)
    for i in range(N):
        arr[i] = list(map(int, input().split())) #인풋 받아 array 생성
    print(f'#{test_case}')
    for j in range(N):
        str1 = ''
        str2 = ''
        str3 = ''
        for k in range(N):
            str1 += str(arr[N-k-1][j])
            str2 += str(arr[N-j-1][N-k-1])
            str3 += str(arr[k][N-j-1])
        print(str1, end=' ')
        print(str2, end=' ')
        print(str3)
 

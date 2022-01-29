"""
2001: 파리 퇴치
"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arrays = []
    paris = []
    for array in range(N):
        arrays.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += arrays[i+k][j+l]
            paris.append(cnt)            
    print(f'#{test_case} {max(paris)}')
    


import sys
sys.stdin = open('2001_input.txt')


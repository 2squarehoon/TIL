"""
1979: 어디에 단어가 들어갈 수 있을까
"""

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arrays = []
    for array in range(N):
        arrays += [list(map(int, input().split()))]
    answer = 0
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arrays[y][x] == 1:
                cnt += 1
            if arrays[y][x] == 0 or x == N-1:
                if cnt == K:
                    answer += 1
                cnt = 0
    for x in range(N):
        for y in range(N):
            if arrays[y][x] == 1:
                cnt += 1
            if arrays[y][x] == 0 or y == N-1:
                if cnt == K:
                    answer += 1
                cnt = 0
    print(f'#{test_case} {answer}')
                

import sys
sys.stdin = open('1979_input.txt')


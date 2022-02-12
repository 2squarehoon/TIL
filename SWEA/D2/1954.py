"""
1954: 달팽이 숫자
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    line = [0] * N
    arr = []
    for i in range(N):
        arr.append(line) # 빈 리스트 만들기
    direction = ['r', 'd', 'l', 'u'] # 방향키 설정
    idx = 0 # 방향키 설정을 위한 인덱스 초기값
    x, y = 0, 0 #x축, y축을 기준으로 한 인덱스


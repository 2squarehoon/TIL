"""
1974: 스도쿠 검증
"""
    
def garo(list): # 가로 숫자들 검증 + 그냥 숫자들 검증
    for x in range(9):
        if sorted(list[x]) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True

def sero(list): # 세로 숫자들 검증
    list1 = []
    for i in range(9):
        list2 = []
        for j in range(9):
            list2.append(list[j][i])
        list1.append(list2) # 리스트를 세로 기준으로 묶어서 새로 만듦
    return garo(list1)

def square(list): # 리스트를 3*3 정사각형 기준으로 묶어서 새로 만듦, 순서는 좌측 상단부터 오른쪽으로
    list3 = [] 
    for i in range(3):
        for j in range(3):
            list3.append([list[i*3][j*3], list[i*3+1][j*3], list[i*3+2][j*3], list[i*3][j*3+1],
             list[i*3+1][j*3+1], list[i*3+2][j*3+1], list[i*3][j*3+2], list[i*3+1][j*3+2], list[i*3+2][j*3+2]])
    return garo(list3)

T = int(input())
for test_case in range(1, T+1):
    sudoku = []
    for numbers in range(9):
        sudoku.append(list(map(int, input().split())))
    print(f'#{test_case} {int(garo(sudoku) and sero(sudoku) and square(sudoku))}')


import sys
sys.stdin = open('1974_input.txt')


M, N = map(int, input().split())
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if not i % j:
            cnt += 1
    if cnt == 2:
        print(i)
        # 시간이슈...
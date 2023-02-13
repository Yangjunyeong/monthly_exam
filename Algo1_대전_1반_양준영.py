T = int(input()) # 테스트케이스 입력

for tc in range(1, T+1): # 케이스 수 만큼 반복을 합니다.
    N, M = map(int, input().split()) # 도화지 크기와 도장을 찍은 횟수를 입력합니다.
    arr = [[0] * N for _ in range(N)]  # N * N 만큼의 빈 도화지를 만듭니다.
    stamp_lst = []
    for i in range(M):
        stamp_lst.append(list(map(int, input().split()))) # 왼쪽 모서리와 너비, 높이를 입력합니다.

    # 도장 찍는 횟수만큼 반복하여 도장을 찍습니다.
    for i in stamp_lst:  # 각각 저장된 스탬프 정보를 하나씩 가져옵니다.
        for r in range(i[3]):  # i[3]은 높이를 나타내고 높이의 길이만큼 반복합니다.
            for c in range(i[2]):  # i[2]는 너비를 나타내고 너비의 길이만큼 반복합니다.
                arr[i[0]+r][i[1]+c] = 1  # 해당하는 칸을 0에서 1로 수정합니다.
    # 도장에 찍힌 칸 수를 확인합니다.
    cnt = 0   # 초기값을 0으로 설정합니다.
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:   # 도장이 있을때마다 하나씩 카운트를 합니다.
                cnt += 1
    # 양식에 맞춰 출력합니다.
    print(f'#{tc} {cnt}')







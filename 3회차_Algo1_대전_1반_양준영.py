dr = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방향 위치정보: 좌상,상,우상, 좌, 우, 좌하, 하, 우하
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
T = int(input())   # 지도의 개수

for tc in range(1, T+1):
    n = int(input())  # 지도의 크기
    map_lst = [list(map(int, input().split())) for _ in range(n)]  # 지도의 정보를 저장합니다.
    mx_height = []  # 봉우리의 정보를 저장할 리스트를 생성합니다.
    for r in range(1, n-1):     # 봉우리는 주변에 8개의 구역이 필요하므로 가장자리는 배제하고 델타를 확인합니다.
        for c in range(1, n-1):
            cnt = 0
            for k in range(8):   # 현재 지점에서 8방향의 정보를 탐색합니다.
                nr = r + dr[k]
                nc = c + dc[k]
                if map_lst[r][c] > map_lst[nr][nc]:   # 비교하는 지역보다 현재 지점이 크다면 1씩 더합니다.
                    cnt += 1

            if cnt == 8:  # 주변 8방향에 있는 지점보다 현재 지점이 더 크다면 봉우리 리스트에 넣습니다.
                mx_height.append(map_lst[r][c])

    if len(mx_height) == 0 or len(mx_height) == 1:  # 봉우리가 한 개 거나 없으면 -1을 출력합니다
        print(f'#{tc} -1')
    else:
        result = max(mx_height) - min(mx_height)  # 아니라면 최대 봉우리와 최소 봉우리의 차이를 저장합니다.
        print(f'#{tc} {result}')



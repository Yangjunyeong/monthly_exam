dr = [0, 1, 0, -1]  # 로봇은 우하좌상의 순서로 움직인다.
dc = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T+1):
    n = int(input())   # 구역의 크기를 입력받는다.
    map_lst = [list(map(int, input().split())) for _ in range(n)]  # 이동정보를 입력받는다.
    stack = [(0, 0)]  # 반복문의 진입을 위해 처음 출발값을 스택에 넣는다.
    num_lst = []   # 이동한 현재 위치를 저장할 리스트를 만든다.
    while stack:   # 스택에 남는게 없다면 더 이상 이동할 곳이 없다는걸 의미한다.
        r, c = stack.pop()     # 현재 위치의 행과 열을 변수로 받는다. r=행 c=열
        num_lst.append(map_lst[r][c])  # 현재 위치를 저장한다.
        nr = r + dr[map_lst[r][c]]  # 현재 위치에서 이동해야할 위치를 변수로 받는다.
        nc = c + dc[map_lst[r][c]]
        # 이동해야할 위치가 경계 안에 있는지 그리고 방문한 적이 있는지 확인한다.
        if 0 <= nr < n and 0 <= nc < n and map_lst[nr][nc] != 9:
            stack.append((nr, nc))
            map_lst[r][c] = 9  # 다음에 방문할 곳이 있다면 현재 있는 곳을 9로 표시한다

    result = []  # 최종 결과를 담을 리스트를 생성

    for i in num_lst:
        if len(result) == 0:  # 최종결과 스택이 비었으면 담는다.
            result.append(i)
        elif result[-1] != i:   # 최종결과 스택의 마지막 요소와 i와 다르다면 스택에 담는다.
            result.append(i)
    print(f'#{tc}', *result)





T = int(input())

for tc in range(1, T+1):
    N, K, A, B = map(int, input().split())  # N은 하늘의 크기, K는 처음 카메라가 찍을 수 있는 영역
    # A와 B는 초점의 위치
    sky = [list(input().split()) for _ in range(N)]  # 하늘에 떠 있는 별의 정보를 입력
    star = 0  # 하늘에 떠있는 별의 총 개수를 구한다.
    for r in range(N):
        for c in range(N):
            if sky[r][c] == '*':
                star += 1
    ans = -1   # 확대 횟수를 받을 변수를 생성한다.
    # -1로 초기값을 잡은 이유는 처음 확대를 안했을떄 사진을 찍었을때 별이 다 담기지 않았을떄
    # 문제에서 -1로 출력하라고 해서 초기값을 -1로 설정했다.
    while K >= 1:  # 사진을 최대한 확대 했을떄 까지 반복하여 사진을 촬영한다.
        cnt = 0   # 카메라 줌 안에 별의 개수를 확인할 변수를 입력
        for r in range(K):
            for c in range(K):
                # 사진이 하늘의 경계에 있는 지 체크하고
                # 사진의 좌상단부터 우하단까지 사진 안의 별의 개수를 체크
                if 0 <= A - (K//2) + r < N and 0 <= A - (K//2) + c < N and \
                        sky[A - (K//2) + r][B - (K//2) + c] == '*':
                    cnt += 1
        if cnt == star:   # 사진 안의 별의 개수와 하늘의 별의 개수가 일치하는지 확인
            ans += 1    # 일치한다면 확대 횟수를 카운팅 한다.
            K -= 2   # 줌이 확대 되면 2씩 가로 세로 길이를 줄인다.
            continue
        else:
            break
    print(f'#{tc}', ans)



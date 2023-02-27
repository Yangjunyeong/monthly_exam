T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N, M은 행과 열의 개수를 입력받습니다.
    garden = [list(map(int, input().split())) for _ in range(N)]  # 정원에 심는 나무의 비용을 입력받습니다.

    cost = 0  # 총 비용을 적을 변수를 생성합니다.
    cnt = 0  # 총 개수를 적을 변수를 생성합니다.
    expensive = 0  # 제일 비싼 나무의 가격을 저장할 변수를 생성합니다.
    column = 0     # 제일 비싼 나무의 가격이 있는 열을 저장합니다.

    for c in range(0, M, 2):  # 왼쪽부터 한 줄씩 건너뛰면서 심으므로 짝수 번쨰 인덱스 열만 확인합니다.
        for r in range(N):
            cost += garden[r][c]   # 비용을 계속해서 더합니다.
            cnt += 1   # 개수를 셉니다.
            if expensive <= garden[r][c]:
                expensive = garden[r][c]   # 가장 비싼 나무의 가격을 저장합니다
                column = c   # 그 열을 저장합니다.

    print(f'#{tc}', cost, cnt, expensive, column+1)
    # 원래 나무 열의 번호는 1부터 시작하기에 리스트의 열에 1을 더해서 출력합니디.



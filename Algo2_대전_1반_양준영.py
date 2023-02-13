T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)] # 빈 10 * 10배열을 만듭니다.
    N = int(input())
    r1, c1 = map(int, input().split())  # 처음 망치의 위치를 입력합니다.


    point = 0   # 점수를 계산할 값을 초기화 한다.
    for i in range(N):
        A, B, K = map(int, input().split()) # 두더지의 위치와 있는 시간을 입력합니다.
        move_distance = 0  # 움직이는 거리를 계산합니다.
               # 이동거리와 K가 일치할때 까지 반복을 합니다.
        while r1 != A: # 가로의 위치가 일치할때 까지 움직인다.
            if move_distance == K:
                break
            if r1 > A:
                r1 -= 1
                move_distance += 1
            elif r1 < A:
                r1 += 1
                move_distance += 1

            if r1 == A and c1 == B:
                point += 1
                break


        while c1 != B:  # 세로의 위치가 일치할때 까지 움직인다.

            if move_distance == K:
                break

            if c1 > B:
                c1 -= 1
                move_distance += 1
            elif c1 < B:
                c1 += 1
                move_distance += 1

            if r1 == A and c1 == B:
                point += 1
                break


    print(f'#{tc} {point}')


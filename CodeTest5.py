def solution(friends, gifts):
    n = len(friends)
    gift_record = [[0] * n for _ in range(n)]  # 선물 주고받은 기록 저장
    gift_index = {name: idx for idx, name in enumerate(friends)}  # 친구 이름에 대한 인덱스 매핑

    # 선물 주고받은 기록 저장
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx = gift_index[giver]
        receiver_idx = gift_index[receiver]
        gift_record[giver_idx][receiver_idx] += 1

    # 선물 지수 계산
    gift_scores = [0] * n
    for i in range(n):
        given = sum(gift_record[i])  # i번 친구가 준 선물의 총합
        received = sum(gift_record[j][i] for j in range(n))  # i번 친구가 받은 선물의 총합
        gift_scores[i] = given - received

    # 다음 달 받을 선물 수 예측
    next_gifts = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if gift_record[i][j] > gift_record[j][i]:
                next_gifts[i] += 1
            elif gift_record[i][j] < gift_record[j][i]:
                next_gifts[j] += 1
            else:
                if gift_scores[i] > gift_scores[j]:
                    next_gifts[i] += 1
                elif gift_scores[i] < gift_scores[j]:
                    next_gifts[j] += 1

    return max(next_gifts)

def solution(storage, usage, change):
    total_usage = usage  # 시작 시 총 사용량은 초기 사용량으로 설정
    for i in range(len(change)):
        usage = usage * (1 + change[i] / 100)  # 사용량 변화 적용
        total_usage = usage  # 변화된 사용량이 총 사용량이 됨
        if total_usage > storage:
            return i  # 초과 시 인덱스 반환
    return -1  # 초과가 없으면 -1 반환


# 입력값
storage = 1000
usage = 2000
change = [-10, 25, -33]

# 실행 결과
print(solution(storage, usage, change))  # 출력: 1

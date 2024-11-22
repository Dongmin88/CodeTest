def diff_int_max(diffs):
    max_value = float('-inf')
    for num in diffs:
        if num >= max_value:
            max_value = num
    return max_value


def diff_int_min(diffs):
    min_value = float('inf')
    for num in diffs:
        if num <= min_value:
            min_value = num
    return min_value


def solution(diffs, times, limit):
    max_level = diff_int_max(diffs)
    min_level = diff_int_min(diffs)
    mid_level = (max_level + min_level) // 2
    print(mid_level)
    spend_times = 0

    while True:
        for x in range(len(diffs)):
            if x == 0:
                if diffs[x] <= mid_level:
                    spend_times = times[x]
                else:
                    spend_times = (diffs[x] - mid_level) * times[x]
            else:
                if diffs[x] <= mid_level:
                    spend_times += times[x]
                else:
                    spend_times += (diffs[x] - mid_level) * (times[x - 1] + times[x]) + times[x]

        if spend_times > limit:
            spend_times = 0
            next_level = (mid_level + max_level) // 2

            if mid_level == min_level:
                mid_level = next_level + 1
                break

            min_level = mid_level
            mid_level = next_level
            print(f"{min_level} {mid_level} {max_level}")
            continue
        else:
            spend_times = 0
            next_level = (mid_level + min_level) // 2

            if mid_level == max_level:
                mid_level = next_level
                break

            max_level = mid_level
            mid_level = next_level
            print(f"{min_level} {mid_level} {max_level}")
            continue

    print(mid_level)
    return mid_level

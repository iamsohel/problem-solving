def find_longest_substring(s: str) -> int:
    longest = 0
    l = 0
    n = len(s)
    sett = set()
    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        current_window = (r - l) + 1  # use this formula
        longest = max(current_window, longest)
        sett.add(s[r])
    return longest


s = "abcabcbb"

result = find_longest_substring(s)
print(result)


def find_maximum_sum_and_avg_of_sub_array(nums, k):
    sum = 0
    n = len(nums)
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    sum = current_sum
    avg = sum / k

    for i in range(k, n):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        sum = max(current_sum, sum)
        avg = max(avg, current_sum/k)

    return sum, avg


result2 = find_maximum_sum_and_avg_of_sub_array([2, 1, 5, 1, 3, 2], k=3)
print(result2)

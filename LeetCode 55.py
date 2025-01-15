from typing import List


def canJump(nums: List[int]) -> bool:
    n = len(nums)
    last_digit = n - 1
    cur_max = 0

    # DP solution
    for i in range(n):
        if i > cur_max:
            return False
        cur_max = max(cur_max, i + nums[i])
        if cur_max >= last_digit:
            return True
    return False



nums: List[int] = [2, 3, 1, 1, 4]
result = canJump(nums)
print("The final result should be: True, because jump 1 step from index 0 to 1, then 3 steps to the last index.")
print("The final result is:", result)




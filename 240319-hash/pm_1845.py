def solution(nums):
    N = len(nums)
    num_set = set(nums)
    if len(num_set) > N / 2:
        return N / 2
    else:
        return len(num_set)
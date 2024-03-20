def solution(numbers, target):
    operators = ['+', '-']
    cnt = 0
    def bT(idx, sums):
        nonlocal cnt
        if idx == len(numbers):
            if sums == target:
                cnt += 1
                return
            else:
                return
        for i in range(2):
            temp = sums
            if i == 0:
                sums += numbers[idx]
            else:
                sums -= numbers[idx]
            bT(idx + 1, sums)
            sums = temp
    bT(0,0)
    return cnt
                
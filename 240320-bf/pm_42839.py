from itertools import permutations  
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**(0.5) + 1)):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        candidate = set(permutations(numbers, i+1))
        for cand in candidate:
            if isPrime(int(''.join(cand))):
                answer.append(int(''.join(cand)))
    
    return len(set(answer))
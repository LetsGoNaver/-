def solution(clothes):
    dictionary = {}
    for cloth in clothes:
        if cloth[1] not in dictionary:
            dictionary[cloth[1]] = 1
        else:
            dictionary[cloth[1]] += 1
    
    answer = 1
    for k, v in dictionary.items():
        answer *= (v + 1)    
    
    return answer - 1
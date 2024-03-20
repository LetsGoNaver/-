def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for i in range(len(citations)):
        if i+1 <= citations[i]:
            if len(citations) - (i+1) <= (i+1):
                h = i + 1
        else:
            break

    return h
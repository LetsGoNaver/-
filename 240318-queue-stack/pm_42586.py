def solution(progresses, speeds):
    n = len(progresses)
    cursor = 0
    cnt = 1
    
    answer = []
    
    while True:
        if progresses[cursor] == 100:
            if cursor + 1 < n:
                if progresses[cursor + 1] == 100:
                    cnt += 1
                    cursor += 1
                else:
                    answer.append(cnt)
                    cnt = 1
                    cursor += 1
            else:
                answer.append(cnt)    
                break
        else:
            for i in range(n):
                if progresses[i] + speeds[i] > 100:
                    progresses[i] = 100
                else:
                    progresses[i] += speeds[i]
            
    return answer
    
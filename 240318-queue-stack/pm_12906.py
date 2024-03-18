def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
            continue
        if answer[-1] != a:
            answer.append(a)
    return answer
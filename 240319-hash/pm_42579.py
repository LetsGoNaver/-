def solution(genres, plays):
    answer = []

    n = len(genres)
    total_play_num={g:0 for g in genres}
    genre_info = {g:[] for g in genres}

    for i in range(n):
        total_play_num[genres[i]]+=plays[i]
        genre_info[genres[i]].append(i)

    total_play_num = sorted(total_play_num.items(), key=lambda x:x[1], reverse=True)

    for g, _ in total_play_num:
        play_index, play_time = genre_info[g],[]
        for i in genre_info[g]:
            play_time.append(plays[i])
        candidate = sorted(list(zip(play_index,play_time)), key=lambda x:x[1], reverse=True)
        play_index, play_time = zip(*candidate)

        if len(play_index)==1:
            answer.append(play_index[0])
            continue
        if play_time[0]==play_time[1]:
            answer.append(min(play_index[0],play_index[1]))
            answer.append(max(play_index[0],play_index[1]))
            continue
        answer.append(play_index[0])
        answer.append(play_index[1])

    return answer

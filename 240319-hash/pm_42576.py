def solution(participant, completion):
    hash_table = 0
    for part in participant:
        hash_table += hash(part)
    for compl in completion:
        hash_table -= hash(compl)
    
    for part in participant:
        if hash(part) == hash_table:
            return part
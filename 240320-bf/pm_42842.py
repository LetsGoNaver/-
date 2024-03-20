def rulerB(x, y):
    return 2*(x+y) - 4

def rulerY(x, y):
    return (x-2) * (y-2)

def solution(brown, yellow):
    candidate = []
    for x in range(3, 2500):
        for y in range(0, x+1):
            if rulerB(x,y) == brown:
                candidate.append([x,y])
    
    for xy in candidate:
        if rulerY(xy[0], xy[1]) == yellow:
            return xy
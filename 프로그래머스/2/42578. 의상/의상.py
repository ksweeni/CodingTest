def solution(clothes):

    clo = {} 
    for name, kind in clothes:
        if kind in clo.keys():
            clo[kind] += [name]
        else:
            clo[kind] = [name]

    answer = 1
    for _, value in clo.items():
        answer *= (len(value) + 1)

    return answer -1
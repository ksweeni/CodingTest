def solution(board, skill):
    M, N = len(board[0]), len(board)

    tmp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for type, r1, c1, r2, c2, degree in skill :
        if type == 1 :
            tmp[r1][c1] += (-degree)
            tmp[r2+1][c2+1] += (-degree)
            tmp[r1][c2+1] -= (-degree)
            tmp[r2+1][c1] -= (-degree)
        else:
            tmp[r1][c1] += degree
            tmp[r2+1][c2+1] += degree
            tmp[r1][c2+1] -= degree
            tmp[r2+1][c1] -= degree

    #가로 누적합
    for j in range(0,N+1) :
        for i in range(1,M+1) :
            tmp[j][i] += tmp[j][i-1]

    #세로 누적합
    for i in range(0,M+1) :
        for j in range(1,N+1) :
            tmp[j][i] += tmp[j-1][i]


    answer = 0
    for i in range(N) :
        for j in range(M) :
            if board[i][j] + tmp[i][j] > 0 :
                answer += 1
    return answer
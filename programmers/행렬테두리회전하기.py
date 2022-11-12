def solution(rows, columns, queries):
    answer = []
    array = [[0] * columns for _ in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            array[i][j] = k
            k += 1

    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        min_num = array[x1][y1]  # 임의로
        # 상단
        temp = array[x1][y2]
        for i in range(y1, y2 - 1):
            move = array[x1][i]
            array[x1][i + 1] = move
            min_num = min(min_num, move)
        # 우
        array[x1 + 1][y2] = temp
        temp = array[x2][y2]
        for i in range(x1 + 1, x2 - 1):
            move = array[i][y2]
            array[i + 1][y2] = move
            min_num = min(min_num, move)

        # 하단
        array[x2][y2 - 1] = temp
        temp = array[x2][y1]
        for i in range(y2 - 1, y1 - 1, -1):
            move = array[x2][i]
            array[x2][i - 1] = move
            min_num = min(min_num, move)
        # 좌
        array[x2 - 1][y1] = temp
        for i in range(x2 - 1, x1 - 1, -1):
            move = array[i][y1]
            array[i - 1][y1] = move
            min_num = min(min_num, move)

        answer.append(min_num)
    return answer
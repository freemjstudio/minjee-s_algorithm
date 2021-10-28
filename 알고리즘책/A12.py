def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥일 때
            # 바닥 위 혹은 보의 한쪽끝부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 보일때
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽끝부분이 다른 보와 동시 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, op = frame
        if op == 0:  # 삭제하는 경우
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if op == 1:  # 추가하는 경우
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)
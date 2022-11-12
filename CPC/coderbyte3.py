from collections import defaultdict


def ArrayChallenge(strArr):
    tree = dict()
    flag = True
    parent = defaultdict(int)  # appear 한 횟수를 카운트
    child = defaultdict(int)

    for edge in strArr:
        if edge[3] not in tree:
            tree[edge[3]] = [edge[1]]
        else:
            tree[edge[3]].append(edge[1])
        parent[edge[3]] += 1
        child[edge[1]] += 1

    for key, value in tree.items():
        if len(value) > 2:
            flag = False  # 자식 노드가 2개 이상이면 false
    for key, value in parent.items():
        if value > 2:  # parent 로 2번 까지만 가능
            flag = False
    for key, value in child.items():
        if value >= 2:
            flag = False
    if flag:
        return "true"
    else:
        return "false"


# keep this function call here
print(ArrayChallenge(input()))
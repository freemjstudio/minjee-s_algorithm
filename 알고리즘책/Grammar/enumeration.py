def mostBalancedPartition(parent, files_size):
    def helper(node, adj, file_sizes):
        queue = [node]
        weight = 0
        while queue:
            index = queue.pop()
            weight += file_sizes[index]
            if index in adj:
                queue.extend(adj[index]) # extend는 iterable 타입을 추가해줄 떄 사용한다.
        return weight
    adj = {}
    edges = []
    for index, p in enumerate(parent):
        edges.append((p, index))
        if p in adj:
            adj[p].append(index) # 부모를 기준으로 인접 그래프 향태 
        else:
            adj[p] = [index]

    total_weight = sum(files_size)
    min_diff = sum(files_size)
    for e in edges:
        p, c = e
        adj[p].remove(c) # index를 삭제했을 떄 -> 연결 끊기
        w1 = helper(c, adj, files_size) # c와 연결되어 있는 노드들의 value 합을 w1에 저장
        min_diff = min(min_diff, abs(total_weight-w1*2))
        adj[p].append(c)
    return min_diff
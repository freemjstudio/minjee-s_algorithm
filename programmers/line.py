for k in range(8):
    nx = fx[k] + i
    ny = fy[k] + j
    if 0 <= nx < n and 0 <= ny < n and fire_array[nx][ny] == 0:
        fire_array[nx][ny] = 1
        fire_visited[nx][ny] = True
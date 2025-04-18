from collections import deque

def is_path_possible(maze):
    if maze[0][0] == 1 or maze[-1][-1] == 1:
        return False

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue, visited = deque([(0, 0)]), set([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if (x, y) == (len(maze)-1, len(maze[0])-1):
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False

def shortest_path_length(maze):
    if maze[0][0] == 1 or maze[-1][-1] == 1:
        return -1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue, visited = deque([(0, 0, 1)]), set([(0, 0)])

    while queue:
        x, y, path_len = queue.popleft()
        if (x, y) == (len(maze)-1, len(maze[0])-1):
            return path_len
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path_len + 1))

    return -1
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print("Is there a valid path?", is_path_possible(maze))
print("Shortest path length:", shortest_path_length(maze))  

import collections, pdb


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        # pdb.set_trace()
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
        # pdb.set_trace()

wall, clear, goal = "#", ".", "*"
width, height = 10, 5
grid = ["..........",
        "...#...##.",
        "..##...#..",
        ".....###..",
        "......*..."]
path = bfs(grid, (0, 0))
print(path)
# [(5, 2), (4, 2), (4, 3), (4, 4), (5, 4), (6, 4)]
lot = [[1,1,1,1,1,1,1],
       [1,1,0,1,1,1,1],
       [0,1,1,0,0,0,1],
       [0,0,1,1,1,1,9],]

def bfs(grid, start):
    # queue=[start]
    width = len(lot[0])
    height = len(lot)
    queue = [[start]]
    seen = set([start])
    loop_limit = 3000
    count=0
    while queue and count < loop_limit:
        path = queue.pop(0)
        x, y = path[-1]
        if lot[y][x] == 9:
            return (path,len(path))
        for x2, y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and lot[y][x] != 0 and (x2,y2) not in seen:
                queue.append(path + [(x2,y2)])
                seen.add((x2,y2))
        count=count+1
        #print(count)
        #print(path)
    return ["we didn't get to finish",path]
    


shortest_path = bfs(lot, (0,0))
print(shortest_path)


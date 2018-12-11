
def spiral(n=4):
    matrix = [[0 for i in range(4)] for i in range(4)]
    width=len(matrix[0])
    height=len(matrix)
    
    values_to_drop = list(range(1,4**2+1))
    position = (0,0)
    seen=[]
    direction = 'right'
    premature_count = 0

    def move(direction='right', position=(1,1)):
        # Move one space
        if direction == 'right':
            position = (position[0]+1, position[1])
        elif direction == 'left':
            position = (position[0]-1, position[1])
        elif direction == 'down':
            position = (position[0], position[1]+1)
        elif direction == 'up':
            position = (position[0], position[1]-1)
        print('position_next',position)
        return position

    while(len(values_to_drop) != 0):
        if premature_count == 13 : break
        
        print('position', position)
        print('direction', direction)
        seen.append(position)
        print('seen', seen)
        new_value = values_to_drop.pop(0)
        print('new_value', new_value)

        matrix[position[1]][position[0]] = new_value
        print('matrix', matrix)

        #If you hit a wall turn right
        if (position[0] == width-1 and direction == 'right') or \
            (position[1] == height-1 and direction == 'down') or \
            (position[0] == 0 and direction == 'left') or \
            (position[1] == 0 and direction == 'up') or \
            position in seen:
            #make right hand turns only
            turn_direction = {'right':'down','down':'left','left':'up','up':'right'}
            direction = turn_direction[direction]

        position = move(direction, position)
        premature_count = premature_count + 1

    return matrix


print(spiral(4))





# lot = [[1,1,1,1,1,1,1],
#        [1,1,0,1,1,1,1],
#        [0,1,1,0,0,0,1],
#        [0,0,1,1,1,1,9],]

# def bfs(grid, start):
#     # queue=[start]
#     width = len(lot[0])
#     height = len(lot)
#     queue = [[start]]
#     seen = set([start])
#     loop_limit = 3000
#     count=0
#     while queue and count < loop_limit:
#         path = queue.pop(0)
#         x, y = path[-1]
#         if lot[y][x] == 9:
#             return (path,len(path))
#         for x2, y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
#             if 0 <= x2 < width and 0 <= y2 < height and lot[y][x] != 0 and (x2,y2) not in seen:
#                 queue.append(path + [(x2,y2)])
#                 seen.add((x2,y2))
#         count=count+1
#         print(count)
#         print(path)
#     return ["we didn't get to finish",path]
    


# shortest_path = bfs(lot, (0,0))


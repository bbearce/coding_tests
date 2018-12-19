
def spiral(n=5):
    matrix = [[0 for i in range(n)] for i in range(n)]
    width=len(matrix[0])
    height=len(matrix)
    
    values_to_drop = list(range(1,n**2+1))
    position = (0,0)
    seen=[]
    direction = 'right'
    premature_count = 0

    def move(direction='right', position=(0,0)):
        # Move one space
        if direction == 'right':
            position = (position[0]+1, position[1])
        elif direction == 'left':
            position = (position[0]-1, position[1])
        elif direction == 'down':
            position = (position[0], position[1]+1)
        elif direction == 'up':
            position = (position[0], position[1]-1)
        return position

    while(len(values_to_drop) != 0):
        # if premature_count == 16 : break

        new_value = values_to_drop.pop(0)

        matrix[position[1]][position[0]] = new_value

        #If you hit a wall turn right
        if (position[0] == width-1 and direction == 'right') or \
            (position[1] == height-1 and direction == 'down') or \
            (position[0] == 0 and direction == 'left') or \
            (position[1] == 0 and direction == 'up') or \
            (move(direction, position) in seen):
            #make right hand turns only
            turn_direction = {'right':'down','down':'left','left':'up','up':'right'}
            direction = turn_direction[direction]
        
        seen.append(position)
        position = move(direction, position)
        # premature_count = premature_count + 1

    [print(i) for i in matrix]
    return True

print(spiral(9))
# print(spiral(100)[50][49])

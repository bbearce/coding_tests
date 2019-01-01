
# rects = [[(0,0), (1,1)],
#          [(0,0), (2,2)],
#          [(0,0), (3,3)]] 

rects = [[(5,6), (296,492)], 
         [(299,496), (100,200)]] 



# Solve for top left corner coordinates of each square

# The easy to see way
# coor = []
# for i in range(lw[0]):
#     for j in range(lw[1]):
#         coor.append((i,j))

# List comprehension
def get_coordinates(rect=[(0,0), (0,0)]):
    coor = [(rect[0][0]+i,rect[0][1]+j) for j in range(rect[1][1]) for i in range(rect[1][0])]
    return coor
# Get all rects coordinates
rects_coors = [get_coordinates(r) for r in rects]

area = 0
n = len(rects_coors)
seen = set()
while n > 1:
    coors_in_common = set(rects_coors[n-1]) & set(rects_coors[n-2])
    new_coors = coors_in_common - seen 
    area += len(new_coors)
    seen = set(rects_coors[n-1]) | set(rects_coors[n-2])
    n -= 1

print("area of overlap is: {}".format(area))

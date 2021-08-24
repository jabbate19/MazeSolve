# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import sys
import Node


# Edit
img = 0;
map = 0
height = 0;
width = 0;
# h,r
start = [ 1, 1 ]
end = [ 197, 199 ]
was_here = 0
path = []
tree = Node.Node( None )

def print_hi( name ):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def img_to_num( img_name ):
    global map, height, width, img, cuf, was_here, path
    img = cv2.imread( img_name )
    map = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    # cv2.imwrite('g.png', map)
    dim = map.shape
    height = dim[0]
    width = dim[1]
    was_here = [ [1 for x in range( width )] for y in range(height) ]
    path = [[1 for x in range(width)] for y in range(height)]
    for h in range( height ):
        for r in range( width ):
            #print( str(h) + ', ' + str(r) + ' Val: ' + str(map[h][r]) )
            if (h != 0 and h != height and r != 0 and r != width and map[h][r] > 0 ):
                if is_junction(map, h, r):
                    # Junct
                    map[h][r] = 2
                    img[h][r] = [255, 0, 0]
                else:
                    map[h][r] = 1

    for h in range(height):
        for r in range(width):
            if ( h == start[0] and r == start[1] ):
                #map[h][r] = 1
                img[h][r] = [0, 255, 0]
            elif ( h == end[0] and r == end[1] ):
                #map[h][r] = 1
                img[h][r] = [0, 0, 255]


def img_to_num_2( ):
    global tree
    tree.insert( start )
    print( tree.data[0] )
    print( tree.data[1] )
    tree = node_search( tree, None )


def node_search( s_node, s_dir ):
    if connected_junct( s_node.data, 0 ) and s_dir != 2:
        s_node.insert( node_search( Node.Node( get_junct( s_node.data, 0 ) ), 0 ) )
    if connected_junct( s_node.data, 1 ) and s_dir != 3:
        s_node.insert( node_search( Node.Node( get_junct( s_node.data, 1 ) ), 1 ) )
    if connected_junct( s_node.data, 2 ) and s_dir != 0:
        s_node.insert( node_search( Node.Node( get_junct( s_node.data, 2 ) ), 2 ) )
    if connected_junct( s_node.data, 3 ) and s_dir != 1:
        s_node.insert( node_search( Node.Node( get_junct( s_node.data, 3 ) ), 3 ) )
    return s_node


# 0 = North, 1 = East, 2 = South, 3 = West
def connected_junct( point, dir ):
    space = 1
    if dir == 0:
        #print(point[0])
        #print(type(point), point.__dict__)
        while map[ point[ 0 ] - space ][ point[ 1 ] ] == 1:
            space += 1

        if map[point[0] - space][point[1]] == 0:
            return False
        elif map[point[0] - space][point[1]] == 2:
            return True
    elif dir == 1:
        while map[point[0]][point[1]+space] == 1:
            space += 1
        if map[point[0]][point[1]+space] == 0:
            return False
        elif map[point[0]][point[1]+space] == 2:
            return True
    elif dir == 2:
        while map[point[0] + space][point[1]] == 1:
            space += 1
        if map[point[0] + space][point[1]] == 0:
            return False
        elif map[point[0] + space][point[1]] == 2:
            return True
    elif dir == 3:
        while map[point[0]][point[1] - space] == 1:
            space += 1
        if map[point[0]][point[1] - space] == 0:
            return False
        elif map[point[0]][point[1] - space] == 2:
            return True


def get_junct( point, dir ):
    space = 1
    if dir == 0:
        while map[point[0] - space][point[1]] == 1:
            space += 1
        return [point[0] - space, point[1]]
    elif dir == 1:
        while map[point[0]][point[1] + space] == 1:
            space += 1
        return [point[0], point[1] + space]
    elif dir == 2:
        while map[point[0] + space][point[1]] == 1:
            space += 1
        return [point[0] + space, point[1]]
    elif dir == 3:
        while map[point[0]][point[1] - space] == 1:
            space += 1
        return [point[0], point[1] - space]


def is_junction( m, y, x ):
    if m[y+1][x] > 0 or m[y-1][x] > 0:
        if m[y][x+1] > 0 or m[y][x-1] > 0:
            return True
    return False


def print_map( m ):
    for h in m:
        print('\n')
        for v in m[h]:
            print( str(v) + ' ', flush=True)


def countJunctions():
    count = 0
    for h in range( height ):
        for r in range( width ):
            if map[h][r] == 2:
                count += 1
    return count


def scan_node( n, e ):
    point = n.data
    if point[1] == end[1] and point[0] == end[0]:
        path.append( point )
        #print(path)
        return True
    else:
        found_it = False
        if n.children is None:
            print("No Children")
        else:
            for c in n.children:
                if scan_node( c, e ):
                    path.insert( 0, point )
                    found_it = True
                    break
        return found_it


def scan_node_2( ):
    nodes_to_visit = [start]
    while len(nodes_to_visit) != 0:
        current_node = nodes_to_visit.pop(0)
        for c in current_node.children:
            nodes_to_visit.append( c )

    return None



sys.setrecursionlimit(25000)
img_to_num("maze100.png")
#cv2.imwrite( 'img100.png', img )
print( countJunctions() )
img_to_num_2()

print( scan_node( tree, end ) )
#path.append([-1,-1])
lh = start[0]
lr = start[1]
for h in range(height):
    for r in range(width):
        if map[h][r] == 2:
            img[h][r] = [255,255,255]


for p in path:
    print( p )
    if len(p) == 2:
        h = p[0]
        r = p[1]
        img[h][r] = [255,255,0]
        if h == lh:
            if( lr < r ):
                for row in range( lr, r ):
                    img[h][row] = [255,255,0]
            else:
                for row in range( r, lr ):
                    img[h][row] = [255,255,0]
        if r == lr:
            if( lh < h ):
                for height in range( lh, h ):
                    img[height][r] = [255,255,0]
            else:
                for height in range( h, lh ):
                    img[height][r] = [255, 255, 0]
        lh = h
        lr = r


img[start[0]][start[1]] = [0,255,0]
img[end[0]][end[1]] = [0,0,255]


cv2.imwrite( 'img_complete100.png', img )




# print( height )
# print( width )
# print_map( map )

# Press the green button in the gutter to run the script.
# Down, Right, BGR
#print( cv2.imread( 'maze.png' )[5,2,0] )
#print( cv2.imread( 'maze.png' )[5,2,1] )
#print( cv2.imread( 'maze.png' )[5,2,2] )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import sys


# Edit
img = 0;
map = 0
height = 0;
width = 0;
# h,r
start = [ 1, 1 ]
end = [ 9, 10 ]
was_here = 0
path = 0

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
                    map[h][r] = 1
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


def solve( y, x ):
    if y == end[0] and x == end[1]: return True
    if map[y][x] == 0 or was_here[y][x] == 0: return False
    was_here[y][x] = True
    if x != 0:
        if solve( y, x-1 ):
            path[y][x] = 2
            return True
    if x != width - 1:
        if solve( y, x+1 ):
            path[y][x] = 2
            return True
    if y != 0:
        if solve( y-1, x ):
            path[y][x] = 2
            return True
    if y != height-1:
        if solve( y+1, x ):
            path[y][x] = 2
            return True
    return False


sys.setrecursionlimit(25000)
img_to_num('maze.png')
cv2.imwrite( 'img.png', img )
print( solve( start[0], start[1] ) )
# print( height )
# print( width )
# print_map( map )

# Press the green button in the gutter to run the script.
# Down, Right, BGR
#print( cv2.imread( 'maze.png' )[5,2,0] )
#print( cv2.imread( 'maze.png' )[5,2,1] )
#print( cv2.imread( 'maze.png' )[5,2,2] )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

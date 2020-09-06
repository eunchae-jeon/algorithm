import sys
# import collections
In = sys.stdin.readline

def segArea(height, start_x, tan):
    left_height = start_x * tan - height 
    right_height = left_height + tan
    if left_height < 0 and right_height > 0:
        w = -left_height/tan
        return (w * -left_height + (1-w) * right_height)/2
    else:
        return abs(left_height)/2 + abs(right_height)/2

while True:
    line = In().rstrip()
    if line == "S":
        break
    heights = []
    h = 0
    for l in line:
        if l == "U":
            h += 1
        elif l == "R":
            heights.append(h)
        else:
            break

    try:
        tan = h / len(heights)
        area = 0
        for x, height in enumerate(heights):
            area += segArea(height, x, tan)
        print("{:.3f}".format(area))
    except:
        print(0)
    


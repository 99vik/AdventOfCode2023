from shapely import Polygon

data = [line.split(' ') for line in open('./day18/data.txt').read().splitlines()]

def calc_vertex1(x, y, direction, steps):
    match direction:
        case 'R':
            return [x + steps, y]
        case 'L':
            return [x - steps, y]
        case 'D':
            return [x, y - steps]
        case 'U':
            return [x, y + steps]
        
def calc_vertex2(x, y, direction, hex_steps):
    steps = int(hex_steps, 16)
    match direction:
        case 0:
            return [x + steps, y]
        case 2:
            return [x - steps, y]
        case 1:
            return [x, y - steps]
        case 3:
            return [x, y + steps]

def calc_area(vertices):
    shape = Polygon(vertices)
    return round(shape.buffer(0.5, join_style='mitre').area)

vertices1 = []
vertices2 = []
point1 = [0, 0]
point2 = [0, 0]
for vertex in data:
    point1 = calc_vertex1(point1[0], point1[1], vertex[0], int(vertex[1]))
    point2 = calc_vertex2(point2[0], point2[1], int(vertex[2][-2]), vertex[2][2:-2])
    vertices1.append(point1)
    vertices2.append(point2)

print(f'Part 1: {calc_area(vertices1)}')
print(f'Part 2: {calc_area(vertices2)}')

def build_empty_grid(height, width):
    row = [0] * (width + 1)
    return [row.copy() for _ in range(0, height + 1)]


def build_tweeners(coords, skip_diagonal=False):
    point_1, point_2 = coords
    if (coords[0][0] != coords[1][0]) and (coords[0][1] != coords[1][1]):
        if skip_diagonal:
            return []

    x_1 = min(point_1[0], point_2[0])
    x_2 = max(point_1[0], point_2[0])

    y_1 = min(point_1[1], point_2[1])
    y_2 = max(point_1[1], point_2[1])

    max_point = (x_2, y_2)

    # TODO: Fix backward diagonals

    track_x = x_1
    track_y = y_1
    tweeners = [(track_x, track_y,)]

    while True:
        if track_x < max_point[0]:
            track_x += 1
        if track_y < max_point[1]:
            track_y += 1

        tweeners.append((track_x, track_y,))

        if (track_x, track_y) == max_point:
            break

    return tweeners


def populate_grid(points):
    grid = build_empty_grid(max_height, max_width)

    for collection in points:
        for point in collection:
            x, y = point
            if (x, y) == (0,0):
                import ipdb; ipdb.set_trace();
            grid[y][x] = (grid[y][x] + 1)

    return grid


def print_grid(grid):
    for row in grid:
        print(row)


with open('in_0.txt', 'r') as file:
    lines = file.read().replace(' ', '').split('\n')
    coord_strings = [tuple(line.split('->')) for line in lines if line]

    coords = []
    max_height = 0
    max_width = 0

    for coord_start, coord_finish in coord_strings:
        x1, y1 = coord_start.split(',')
        x2, y2 = coord_finish.split(',')

        start = (int(x1), int(y1))
        finish = (int(x2), int(y2))

        max_height = max(max_height, int(y1), int(y2))
        max_width = max(max_width, int(x1), int(x2))

        coords.append((start, finish,))

    all_points = []
    for coord_pair in coords:
        tweeners = build_tweeners(coord_pair)
        if tweeners:
            all_points.append(tweeners)

    populated_grid = populate_grid(all_points)

    print_grid(populated_grid)

    maximum = 0
    for row in populated_grid:
        row_max = max(row)
        maximum = max(row_max, maximum)

    counter = 0
    for row in populated_grid:
        for val in row:
            if val >= 2:
                counter += 1

    print(counter)

# 20278 LOW

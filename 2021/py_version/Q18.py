def detect_low_point(datas):
    low_points, low_location = [], []

    for i in range(len(datas)):
        for j in range(len(datas[0])):
            if is_lower(i, j, datas):
                low_points.append(datas[i][j])
                low_location.append((i, j))

    return low_points, low_location


def is_lower(x, y, matrix):
    if y - 1 >= 0:
        if matrix[x][y] >= matrix[x][y - 1]:
            return False

    if y + 1 <= len(matrix[x]) - 1:
        if matrix[x][y] >= matrix[x][y + 1]:
            return False

    if x - 1 >= 0:
        if matrix[x][y] >= matrix[x - 1][y]:
            return False

    if x + 1 <= len(matrix) - 1:
        if matrix[x][y] >= matrix[x + 1][y]:
            return False

    return True


def get_basin_size(datas, matrix):
    tmp = []
    res = 1
    for point in datas:
        tmp.append(calculate_basi_size(point, matrix))

    for i in sorted(tmp, reverse=True)[:3]:
        res *= i
    return res


def calculate_basi_size(point, matrix):
    size = 0
    if point[0] >= 0 and point[1] >= 0 and point[0] < len(matrix) and point[1] < len(matrix[point[0]]):
        if matrix[point[0]][point[1]] != '#' and matrix[point[0]][point[1]] < 9:
            size = 1
            matrix[point[0]][point[1]] = '#'
            size += calculate_basi_size((point[0] + 1, point[1]), matrix)
            size += calculate_basi_size((point[0] - 1, point[1]), matrix)
            size += calculate_basi_size((point[0], point[1] + 1), matrix)
            size += calculate_basi_size((point[0], point[1] - 1), matrix)

    return size


if __name__ == '__main__':
    with open('../input/q17input.in') as f:
        datas = [list(map(int, list(line.strip()))) for line in f.read().strip().split("\n")]
    low, point = detect_low_point(datas)
    # print(sum(low) + len(point))
    print(get_basin_size(point, datas))

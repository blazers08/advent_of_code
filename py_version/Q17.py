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


if __name__ == '__main__':
    with open('../input/q17input.in') as f:
        datas = [list(map(int, list(line.strip()))) for line in f.read().strip().split("\n")]
    low, point = detect_low_point(datas)
    print(sum(low) + len(point))

def moving(plan):
    position, depth = 0, 0

    for key, val in plan:

        if key == 'forward':
            position += int(val)
        elif key == 'down':
            depth += int(val)
        else:
            depth -= int(val)

    return position*depth


if __name__ == '__main__':
    with open('q3input.in') as f:
        plan = [tuple(i.split(' ')) for i in f.read().split('\n')]
    print(moving(plan))

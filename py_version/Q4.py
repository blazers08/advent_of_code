def moving(plan):
    position, depth, aim = 0, 0, 0

    for key, val in plan:

        if key == 'forward':
            position += int(val)
            depth += (aim*int(val))
        elif key == 'down':
            aim += int(val)
        else:
            aim -= int(val)

    return position*depth


if __name__ == '__main__':
    with open('input/q3input.in') as f:
        plan = [tuple(i.split(' ')) for i in f.read().split('\n')]
    print(moving(plan))

def detect(depthreport):
    current = None
    increased, decreased = 0, 0

    for i in depthreport:

        if current is None:
            current = i
        else:
            if current < i:
                increased += 1
            else:
                decreased += 1
            current = i

    return increased


if __name__ == "__main__":
    with open('input/q1input.in') as f:
        report = [int(i) for i in f.read().split('\n')]
    print(detect(report))

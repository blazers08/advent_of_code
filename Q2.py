def detect(depthreport):
    current = None
    increased, decreased = 0, 0

    for i in range(len(depthreport)-3+1):
        tmp = sum(depthreport[i:i+3])
        if current is None:
            current = tmp
        else:
            if current < tmp:
                increased += 1
            elif current > tmp:
                decreased += 1
            else:
                pass
            current = tmp

    return increased


if __name__ == "__main__":
    with open('q1input.in') as f:
        report = [int(i) for i in f.read().split('\n')]
    print(detect(report))

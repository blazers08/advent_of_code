def diagno(report):
    gamma, epsilon = '', ''

    for i in range(len(report[0])):
        a, b = 0, 0
        for item in report:
            if item[i] == '0':
                a += 1
            else:
                b += 1

        if a > b or a == b:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2)*int(epsilon, 2)


if __name__ == '__main__':
    with open('q5input.in') as f:
        report = f.read().split('\n')
    print(diagno(report))

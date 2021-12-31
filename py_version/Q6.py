def diagno(report):
    oxygen = report.copy()
    co2 = report.copy()

    def cal(tmp, cate):
        i = 0
        while len(tmp) > 1:
            zeros, ones = 0, 0

            for item in tmp:
                if item[i] == '0':
                    zeros += 1
                else:
                    ones += 1

            if cate == 'oxy':
                if zeros > ones:
                    tmp = [item for item in tmp if item[i] == '0']
                else:
                    tmp = [item for item in tmp if item[i] == '1']
            else:
                if zeros > ones:
                    tmp = [item for item in tmp if item[i] == '1']
                else:
                    tmp = [item for item in tmp if item[i] == '0']
            i += 1
        return tmp

    return int(cal(oxygen, 'oxy').pop(), 2)*int(cal(co2, 'co').pop(), 2)


if __name__ == '__main__':
    with open('input/q5input.in') as f:
        report = f.read().split('\n')
    print(diagno(report))

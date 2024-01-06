def determine_digit(datas):
    pattern = {}

    for digit in datas:
        if len(digit) == 2:
            pattern[1] = digit
        elif len(digit) == 4:
            pattern[4] = digit
        elif len(digit) == 3:
            pattern[7] = digit
        elif len(digit) == 7:
            pattern[8] = digit

    for digit in datas:
        if len(digit) == 6:
            if set(pattern[4]).issubset(set(digit)):
                pattern[9] = digit
            elif set(pattern[1]).issubset(set(digit)):
                pattern[0] = digit
            else:
                pattern[6] = digit

    for digit in datas:
        if len(digit) == 5:
            if set(digit).issubset(set(pattern[6])):
                pattern[5] = digit
            elif set(pattern[1]).issubset(set(digit)):
                pattern[3] = digit
            else:
                pattern[2] = digit

    return pattern


if __name__ == '__main__':
    with open('../input/q15input.in') as f:
        datas = [str(ele) for ele in f.read().split('\n')]
        segs = [ele.split('|')[0].strip().split(' ') for ele in datas]
        segs1 = [ele.split('|')[1].strip().split(' ') for ele in datas]

    ans = []

    for i in range(len(datas)):
        pattern = determine_digit(segs[i])
        tmp = ''

        for digit in segs1[i]:
            for key, value in pattern.items():
                if set(digit) == set(value):
                    tmp += str(key)

        ans.append(int(tmp))

    print(sum(ans))

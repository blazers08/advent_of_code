def fishcount(data, days):
    day = 0

    while day < days:
        for i in range(len(data)):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            else:
                data[i] -= 1

        day += 1
    return len(data)


if __name__ == '__main__':
    with open('../input/q11input.in') as f:
        fishes = [int(ele) for ele in f.read().split(',')]

    print(fishcount(fishes, 80))

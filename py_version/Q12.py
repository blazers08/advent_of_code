from collections import defaultdict


def fishcount(data, days):
    day = 0
    fishmap = {}

    for fish in data:
        if fish not in fishmap:
            fishmap[fish] = 0
        fishmap[fish] += 1

    while day < days:
        tmp = defaultdict(int)

        for fish, count in fishmap.items():
            if fish == 0:
                tmp[6] += count
                tmp[8] += count
            else:
                tmp[fish-1] += count
        day += 1
        fishmap = tmp

    return sum(fishmap.values())


if __name__ == '__main__':
    with open('../input/q11input.in') as f:
        fishes = [int(ele) for ele in f.read().split(',')]

    print(fishcount(fishes, 256))

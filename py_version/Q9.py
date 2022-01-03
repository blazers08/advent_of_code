import re


def main(data):
    vent_map = {}
    count = 0

    for i in range(0, len(data), 2):
        start = (int(data[i].split(',')[0]), int(data[i].split(',')[1]))
        end = (int(data[i+1].split(',')[0]), int(data[i+1].split(',')[1]))

        # |
        if start[0] == end[0]:
            if start[1] > end[1]:
                for i in range(int(end[1]), int(start[1])+1, 1):
                    pos = (int(start[0]), i)
                    if pos in vent_map:
                        vent_map[pos] += 1
                    else:
                        vent_map[pos] = 1
            else:
                for i in range(int(start[1]), int(end[1])+1, 1):
                    pos = (int(start[0]), i)
                    if pos in vent_map:
                        vent_map[pos] += 1
                    else:
                        vent_map[pos] = 1
        # -
        elif start[1] == end[1]:
            if start[0] > end[0]:
                for i in range(int(end[0]), int(start[0])+1, 1):
                    pos = (i, int(start[1]))
                    if pos in vent_map:
                        vent_map[pos] += 1
                    else:
                        vent_map[pos] = 1
            else:
                for i in range(int(start[0]), int(end[0])+1, 1):
                    pos = (i, int(start[1]))
                    if pos in vent_map:
                        vent_map[pos] += 1
                    else:
                        vent_map[pos] = 1
        else:
            pass

    for ele in vent_map.values():
        if ele >= 2:
            count += 1

    return count


if __name__ == '__main__':
    with open('q9input.in') as f:
        data = f.read()
        data = re.split(r' -> |\n', data)

    print(main(data))

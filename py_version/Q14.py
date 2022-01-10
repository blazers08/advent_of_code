from statistics import mean


def calulate_least_fuel(data):
    means = int(mean(data))
    fuel_cost = []

    for pos in data:
        total = 0
        for i in range(1, abs(pos-means)+1):
            total += i
        fuel_cost.append(total)

    return sum(fuel_cost)


if __name__ == '__main__':
    with open('../input/q13input.in') as f:
        datas = [int(ele) for ele in f.read().split(',')]

    print(calulate_least_fuel(datas))

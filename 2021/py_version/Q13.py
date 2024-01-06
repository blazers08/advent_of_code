from statistics import median


def calulate_least_fuel(data):
    medians = int(median(data))
    fuel_cost = []

    for pos in data:
        fuel_cost.append(abs(pos-medians))

    return sum(fuel_cost)


if __name__ == '__main__':
    with open('../input/q13input.in') as f:
        datas = [int(ele) for ele in f.read().split(',')]

    print(calulate_least_fuel(datas))

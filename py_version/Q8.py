def calculate(number, board):
    for i in board:
        for j in range(len(i)):
            if i[j] == number:
                i[j] = 'x'


def sumofunmarked(board):
    total = 0
    for i in board:
        for j in i:
            if j != 'x':
                total += j

    return total


def check_win(board):
    win = False

    # check -
    for i in board:
        win = all(ele in ['x'] for ele in i)

        if win:
            return win

    # check |
    for i in range(5):
        win = all(ele[i] in ['x'] for ele in board)

        if win:
            return win

    return win


if __name__ == '__main__':
    with open('input/q7input.in') as f:
        ran_num, *tables = f.read().split('\n\n')

    ran_num = [int(i) for i in ran_num.split(',')]
    tables = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in tables]

    last_win = False
    while not last_win:
        for number in ran_num:
            for board in tables:
                calculate(number, board)

            index = 0
            while index < len(tables):
                if check_win(tables[index]):
                    if len(tables) > 1:
                        tables.pop(index)
                    else:
                        last_win = True
                        print(number * sumofunmarked(tables[index]))
                        exit()
                else:
                    index += 1

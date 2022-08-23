def check_brackets(line):
    score = 0
    stack, pairs = [], {'}': '{', ')': '(', ']': '[', '>': '<'}
    pair_score = {')': 3, ']': 57, '}': 1197, '>': 25137}

    complete_score = 0
    complete_bracket = True
    complete_score_map = {')': 1, ']': 2, '}': 3, '>': 4}

    for char in line:
        if char in pairs:
            if not stack or not pairs[char] == stack.pop():
                score += pair_score[char]
                complete_bracket = False
                break
        else:
            stack.append(char)

    # print(stack)

    if stack and complete_bracket:
        for item in stack[::-1]:
            complete_score = complete_score * 5 + complete_score_map[list(pairs.keys())[list(pairs.values()).index(item)]]
            # print(complete_score)
    return complete_score


if __name__ == '__main__':
    mid_score = []
    with open('../input/q19input.in') as f:
        for line in f.read().strip().split("\n"):
            if check_brackets(line) != 0:
                mid_score.append(check_brackets(line))

    print(sorted(mid_score)[len(mid_score)//2])

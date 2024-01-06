def check_brackets(line):
    score = 0
    stack, pairs = [], {'}': '{', ')': '(', ']': '[', '>': '<'}
    pair_score = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for char in line:
        if char in pairs:
            if not stack or not pairs[char] == stack.pop():
                score += pair_score[char]
                break
        else:
            stack.append(char)

    return score


if __name__ == '__main__':
    score = 0
    with open('../input/q19input.in') as f:
        for line in f.read().strip().split("\n"):
            score += check_brackets(line)
    print(score)

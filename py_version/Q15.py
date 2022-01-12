def count_unique_seg(datas):
    count = 0
    for seg in datas:
        for digit in seg:
            if len(digit) in (2, 3, 4, 7):
                count += 1

    return count


if __name__ == '__main__':
    with open('../input/q15input.in') as f:
        datas = [str(ele) for ele in f.read().split('\n')]
        segs = [ele.split('|')[1].strip().split(' ') for ele in datas]

    print(count_unique_seg(segs))

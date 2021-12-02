def count_increases(report, window=1):
    return sum(
        sum(report[i:i+window]) < sum(report[(next := i+1):next+window])
        for i in range(len(report[:-window]))
    )


if __name__ == '__main__':
    report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    assert count_increases(report) == 7
    assert count_increases(report, window=3) == 5

    with open('inputs/day1.txt') as f:
        report = [int(l) for l in f]
        assert count_increases(report) == 1754
        assert count_increases(report, window=3) == 1789

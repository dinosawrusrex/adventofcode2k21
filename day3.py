import math

def prod(*args):
    return math.prod(int(v, base=2) for v in args)

def epsilon(gamma):
    return ''.join({'1': '0'}.get(v, '1') for v in gamma)

def get_gamma(report):
    sum_per_position = []
    for binary in report:
        if not sum_per_position:
            sum_per_position = [0] * len(binary)

        for index, bit in enumerate(binary):
            sum_per_position[index] += int(bit)

    return ''.join(str(int(total >= (len(report)/2))) for total in sum_per_position)

def rating(report, gamma_bit, index=0, use_epsilon=False):
    if len(
        filtered := [b for b in report if b[index] == (epsilon(gamma_bit) if use_epsilon else gamma_bit)]
    ) == 1:
        return filtered.pop()
    return rating(filtered, get_gamma(filtered)[index+1], index=index+1, use_epsilon=use_epsilon)


if __name__ == '__main__':
    report = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

    import math
    gamma = get_gamma(report)
    assert prod(gamma, epsilon(gamma)) == 198
    assert prod(rating(report, gamma[0]), rating(report, gamma[0], use_epsilon=True)) == 230

    with open('inputs/day3.txt') as f:
        report = [l.strip() for l in f]
        gamma = get_gamma(report)
        assert prod(gamma, epsilon(gamma)) == 1458194
        assert prod(rating(report, gamma[0]), rating(report, gamma[0], use_epsilon=True)) == 2829354

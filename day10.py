BRACKETS = {'<': '>', '(': ')', '[': ']', '{': '}'}

ILLEGAL_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_POINTS = {'(': 1, '[': 2, '{': 3, '<': 4}

def trim_line(line):
    for item in BRACKETS.items():
        if (pair := ''.join(item)) in line:
            line = trim_line(line.replace(pair, ''))
    return line

def first_illegal_match(line):
    line = trim_line(line)
    illegals = [b for b in BRACKETS.values() if b in line]
    if illegals:
        return line, ILLEGAL_POINTS[min(illegals, key=lambda b: line.find(b))]
    return line, 0

def filter_illegal(lines):
    incomplete, illegal = [], 0
    for l in lines:
        line, score = first_illegal_match(l.strip())
        if score:
            illegal += score
        else:
            incomplete.append(line)
    return incomplete, illegal

def score_incomplete(incomplete):
    score = 0
    for b in reversed(incomplete):
        score *= 5
        score += COMPLETION_POINTS[b]
    return score

    
if __name__ == '__main__':
    import statistics

    sample = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]

    incomplete, illegal = filter_illegal(sample)
    assert illegal == 26397
    assert statistics.median((score_incomplete(i) for i in incomplete)) == 288957

    with open('inputs/day10.txt') as f:
        incomplete, illegal = filter_illegal(f)
        assert illegal == 166191
        assert statistics.median((score_incomplete(i) for i in incomplete)) == 1152088313

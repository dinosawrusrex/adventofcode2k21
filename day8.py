import collections

NUMBER_TO_SEGMENTS = [
    {0, 1, 2, 4, 5, 6}, # 6
    {2, 5}, # 2
    {0, 2, 3, 4, 6}, # 5
    {0, 2, 3, 5, 6}, # 5
    {1, 2, 3, 5}, # 4
    {0, 1, 3, 5, 6}, # 5
    {0, 1, 3, 4, 5, 6}, # 6
    {0, 2, 5}, # 3
    {0, 1, 2, 3, 4, 5, 6}, # 7
    {0, 1, 2, 3, 5, 6}, # 6
]

def count_simple(entries):
    unique = [len(segment) for i, segment in enumerate(NUMBER_TO_SEGMENTS) if i in {1, 4, 7, 8}]
    count = 0
    total = 0
    for entry in entries:
        signal, output = entry.strip().split(' | ')
        count += len([v for v in output.split() if len(v) in unique])
        total += number_for_output_value(signal, output)
    return count, total

def number_for_output_value(signal, output):
    mapping = map_segment(signal)
    number = ''
    for digit in output.split():
        number += str(NUMBER_TO_SEGMENTS.index({mapping.index(c) for c in digit}))
    return int(number)

def map_segment(signal):
    mapping = [None]*7
    mapping[0] = segment_0(signal)
    mapping[3:5] = segment_3_4(signal)
    mapping[5] = segment_5(signal)
    mapping[2] = segment_2(signal, mapping)
    mapping[1], mapping[6] = segment_1_6(signal, mapping)
    return mapping

def segment_0(signal):
    one, seven = '', ''
    for v in signal.split():
        if len(v) == 2:
            one = v
        if len(v) == 3:
            seven = v
        if one and seven:
            return seven.replace(one[0], '').replace(one[1], '')

def segment_3_4(signal):
    three, four = None, None
    for segment, count in collections.Counter(''.join(v for v in signal.split() if len(v) in [4,5])).items():
        if count == 4:
            three = segment
        if count == 1:
            four = segment
        if three and four:
            return three, four
    return None, None

def segment_5(signal):
    for segment, count in collections.Counter(signal.replace(' ', '')).items():
        if count == 9:
            return segment

def segment_2(signal, known_segment):
    for segment in signal.split():
        if len(segment) == 2:
            return segment.strip(known_segment[5])

def segment_1_6(signal, known_segment):
    one, six = [None]*2
    for segment, count in collections.Counter(
        ''.join(v for v in signal.split() if len(v) == 5)
    ).items():
        if segment not in known_segment:
            if count == 1:
                one = segment
            if count == 3:
                six = segment
            if one and six:
                return one, six
    return None, None


if __name__ == '__main__':
    sample = [
        'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
        'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
        'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
        'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
        'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
        'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
        'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
        'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
        'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
        'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
    ]
    assert count_simple(sample) == (26, 61229)
   
    signal = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
    mapping = map_segment(signal)
    assert mapping == ['d','e','a','f','g','b','c']

    with open('inputs/day8.txt') as f:
        assert count_simple(f) == (375, 1019355)

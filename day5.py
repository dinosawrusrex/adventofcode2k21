import collections

P = collections.namedtuple('P', 'x, y')

def correction(start_value, end_value):
    return 1 if end_value > start_value else -1

def coordinates_travelled(start, end):
    if any(((same_x := start.x == end.x), start.y == end.y)):
        changing_start, changing_end = (start.y, end.y) if same_x else (start.x, end.x)
        return 'same', (
            (start.x, v) if same_x else (v, start.y)
            for v in range(
                changing_start,
                changing_end+correction(changing_start, changing_end),
                correction(changing_start, changing_end)
            )
        )

    if abs(start.x - end.x) == abs(start.y - end.y):
        return 'diagonal', (
            (x, y) for x, y in zip(
                range(start.x, end.x+correction(start.x, end.x), correction(start.x, end.x)),
                range(start.y, end.y+correction(start.y, end.y), correction(start.y, end.y))
            )
        )

    return '', []

def tally_overlaps(vent_lines):
    same_axis = collections.defaultdict(int)
    with_diagonal = collections.defaultdict(int)
    for line in vent_lines:
        start, end = (P(*(int(v) for v in coord.split(','))) for coord in line.strip().split(' -> '))
        dimension, coordinates = coordinates_travelled(start, end)
        if dimension:
            for coord in coordinates:
                if dimension == 'same':
                    same_axis[coord] += 1
                with_diagonal[coord] += 1
    return len([k for k, v in same_axis.items() if v > 1]), len([k for k, v in with_diagonal.items() if v > 1])


if __name__ == '__main__':
    with open('inputs/day5test.txt') as f:
        assert tally_overlaps(f) == (5, 12)

    with open('inputs/day5.txt') as f:
        assert tally_overlaps(f) == (5576, 18144)

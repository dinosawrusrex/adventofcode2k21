import collections

P = collections.namedtuple('P', 'x, y')

def is_lowest(point, heightmap):
    curr = int(heightmap[point.y][point.x])
    for x, y in (pairs := [(0, -1), (0, 1)]) + [reversed(p) for p in pairs]:
        if (adjacent_x := point.x+x) > -1 and (adjacent_y := point.y+y) > -1:
            try:
                if curr >= int(heightmap[adjacent_y][adjacent_x]):
                    return
            except IndexError:
                pass
    return True

def collect_lowest(heightmap):
    return [
        point
        for y, row in enumerate(heightmap)
        for x, _ in enumerate(row)
        if is_lowest(point := P(x, y), heightmap)
    ]

def in_basin(point, heightmap, basin=None):
    basin = basin if basin else set()
    curr = int(heightmap[point.y][point.x])
    if curr != 9:
        basin.add(point)
        for x, y in (pairs := [(0, -1), (0, 1)]) + [reversed(p) for p in pairs]:
            if (adjacent_x := point.x+x) > -1 and (adjacent_y := point.y+y) > -1:
                try:
                    if (adjacent := P(adjacent_x, adjacent_y)) not in basin:
                        basin.update(in_basin(adjacent, heightmap, basin))
                except IndexError:
                    pass
    return basin


if __name__ == '__main__':

    sample = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]

    lowest = collect_lowest(sample)
    assert sum(int(sample[p.y][p.x])+1 for p in lowest) == 15
    assert sorted([len(in_basin(p, sample)) for p in lowest]) == [3, 9, 9, 14]

    with open('inputs/day9.txt') as f:
        heightmap = [l.strip() for l in f.readlines()]
        lowest = collect_lowest(heightmap) 
        assert sum(int(heightmap[p.y][p.x])+1 for p in lowest) == 530

        import math
        assert math.prod(sorted(len(in_basin(p, heightmap)) for p in lowest)[-3:]) == 1019494

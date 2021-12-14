import collections

P = collections.namedtuple('P', 'x, y')
Folds = collections.namedtuple('Folds', 'dimension, fold')

def points_and_fold_instructions(instructions):
    points, folds = [], []
    for i in instructions:
        if (i := i.strip()):
            if ',' in i:
                points.append(P(*(int(v) for v in i.split(','))))
            elif 'fold along' in i:
                i = i.replace('fold along ', '')
                folds.append(Folds(*(int(v) if v.isdigit() else v for v in i.split('='))))
    return points, folds

def simulate_fold(points, folds):
    first = None
    new_points = []
    for fold in folds:
        if new_points:
            points = new_points
            new_points = []
        for point in points:
            if getattr(point, fold.dimension) < fold.fold:
                new_points.append(point)
            else:
                new_value = fold.fold - (getattr(point, fold.dimension) - fold.fold)
                if (new_point := P(point.x, new_value) if fold.dimension == 'y' else P(new_value, point.y)) not in points:
                    new_points.append(new_point)

        if first is None:
            first = len(new_points)
    return first, new_points

def code(folded):
    width = max(p.x for p in folded)
    height = max(p.y for p in folded)
    for y in range(height+1):
        for x in range(width+1):
            print('#' if (x, y) in folded else ' ', end='')
        print()


if __name__ == '__main__':
    sample = [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        '',
        'fold along y=7',
        'fold along x=5',
    ]

    points, folds = points_and_fold_instructions(sample)
    first, folded = simulate_fold(points, folds)
    assert first == 17
    code(folded)

    with open('inputs/day13.txt') as f:
        points, folds = points_and_fold_instructions(f)
        first, folded = simulate_fold(points, folds)
        assert first == 701
        code(folded)

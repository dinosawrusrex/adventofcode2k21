def final_position(course, with_aim=False):
    x, y = 0, 0
    aim = 0

    for step in course:
        direction, unit = step.split()
        unit = int(unit)
        if direction == 'forward':
            x += unit
            y += aim * unit 
        else:
            if with_aim:
                aim += (-1 if direction == 'up' else 1) * unit
            else:
                y += (-1 if direction == 'up' else 1) * unit

    return x * y


if __name__ == '__main__':
    import itertools

    course = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]

    assert final_position(course) == 150
    assert final_position(course, with_aim=True) == 900

    with open('inputs/day2.txt') as f:
        f1, f2 = itertools.tee(f)
        assert final_position(f1) == 2036120
        assert final_position(f2, with_aim=True) == 2015547716

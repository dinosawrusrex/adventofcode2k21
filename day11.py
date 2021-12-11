def neighbours(octopus):
    return (
        (octopus[0]+x, octopus[1]+y)
        for y in range(-1, 2)
        for x in range(-1, 2)
        if (x, y) != (0, 0)
    ) 

def parse_grid(grid):
    return {
        (x, y): int(level)
        for y, row in enumerate(grid)
        for x, level in enumerate(row)
    }

def simultaneous_and_flash_count(grid, end):
    grid = grid.copy()
    count = 0
    step = 0
    while True:
        step += 1
        for octopus in grid:
            grid[octopus] += 1 if grid[octopus] < 9 else -9
        flashed, grid = handle_flash(grid)

        if step <= end:
            count += len(flashed)

        if set(grid.values()) == {0}:
            return step, count

def handle_flash(grid, handled=None):
    handled = handled if isinstance(handled, set) else set()
    if just_flashed := set(k for k, v in grid.items() if v == 0).difference(handled):
        handled.update(just_flashed)
        for o in just_flashed:
            for neighbour in neighbours(o):
                if neighbour not in handled and neighbour in grid:
                    grid[neighbour] += -9 if grid[neighbour] == 9 else 1 if grid[neighbour] else 0
        return handle_flash(grid, handled=handled)
    return handled, grid


if __name__ == '__main__':
    sample = [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526',
    ]

    grid = parse_grid(sample)
    assert simultaneous_and_flash_count(grid, 100) == (195, 1656)

    raw_grid = [
        '8826876714',
        '3127787238',
        '8182852861',
        '4655371483',
        '3864551365',
        '1878253581',
        '8317422437',
        '1517254266',
        '2621124761',
        '3473331514',
    ]
    grid = parse_grid(raw_grid)
    assert simultaneous_and_flash_count(grid, 100) == (788, 1683)

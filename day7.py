import functools
import math
import statistics

def fuel_for_aligning(positions, align, constant=False):
    return sum(
        sum(range(abs(align-position)+1))
        if constant else
        abs(align - position)
        for position in positions
    )

def align_with_least_fuel(positions, constant=False):
    mean = math.floor(statistics.mean(positions))
    stdev = math.ceil(statistics.pstdev(positions, mu=mean))
    minimum = max(0, mean-stdev)
    maximum = min(max(positions), mean+stdev)
    return min(range(minimum, maximum+1), key=functools.partial(fuel_for_aligning, positions, constant=constant))


if __name__ == '__main__':
    positions = [16,1,2,0,4,2,7,1,2,14]
    assert fuel_for_aligning(positions, 2) == 37
    assert fuel_for_aligning(positions, 1) == 41
    assert fuel_for_aligning(positions, 3) == 39
    assert fuel_for_aligning(positions, 10) == 71
    assert align_with_least_fuel(positions) == 2
    assert fuel_for_aligning(positions, align_with_least_fuel(positions)) == 37

    fuel_for_aligning(positions, 5, constant=True) == 168
    fuel_for_aligning(positions, 2, constant=True) == 206
    assert align_with_least_fuel(positions, constant=True) == 5
    assert fuel_for_aligning(positions, align_with_least_fuel(positions, constant=True), constant=True) == 168
    
    with open('inputs/day7.txt') as f:
        positions = [int(p) for p in f.readline().strip().split(',')]
        assert fuel_for_aligning(positions, align_with_least_fuel(positions)) == 347011
        assert fuel_for_aligning(positions, align_with_least_fuel(positions, constant=True), constant=True) == 98363777

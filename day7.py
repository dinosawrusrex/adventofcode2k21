import functools
import math
import statistics

def fuel_for_aligning(positions, align, constant=False):
    if constant:
        return sum(sum(range(abs(align-position)+1)) for position in positions)
    return sum(abs(align - position) for position in positions)

def align_with_least_fuel(positions, constant=False):
    '''
    Heuristic, and minor optimisation.
    Instead of calculating every fuel use from min to max, calculate fuel use within one standard deviation of the mean position.
    Fuel use is always minimal between min and max. Mean is between min and max, so it's probably a good starting point.
    Standard deviation describes the "average" difference a data point would be from the mean.
    So, we can bring the range of calculation down to within a standard deviation around the mean..
    '''
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

import collections

def generate_start(initial):
    start = collections.deque()
    for i in range(7):
        start.appendleft(initial.count(str(i)))
    return start

def simulate(initial, end):
    start = generate_start(initial)
    juvenile = collections.deque([0, 0])
    for _ in range(end):
        to_juvenile = start[-1]
        start.rotate()
        start[0] += juvenile[0]
        juvenile[0] = to_juvenile
        juvenile.rotate()
    return sum(start) + sum(juvenile)


if __name__ == '__main__':
    initial = '3,4,3,1,2'
    assert simulate(initial, 18) == 26
    assert simulate(initial, 80) == 5934
    assert simulate(initial, 256) == 26984457539

    with open('inputs/day6.txt') as f:
        initial = f.readline().strip()
        assert simulate(initial, 80) == 346063
        assert simulate(initial, 256) == 1572358335990

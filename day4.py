import collections


class Bingo(Exception):
    pass


class Board:

    def __init__(self):
        self.numbers = {}
        self.hit = set()
        self.x_hit = collections.defaultdict(lambda: 0)
        self.y_hit = collections.defaultdict(lambda: 0)

    def __contains__(self, number):
        if number in self.numbers:
            self.hit.add(number)
            self.update_hit(number)

    def update_hit(self, number):
        x, y = self.numbers[number]
        self.x_hit[x] += 1
        self.y_hit[y] += 1
        if self.x_hit[x] == 5 or self.y_hit[y] == 5:
            raise Bingo(f'{self.score(number)}')
            
    def score(self, last_hit):
        return sum(map(int, set(self.numbers).difference(self.hit))) * int(last_hit)


def parse_input(input_file):
    draw = []
    boards = []
    with open(input_file) as f:
        y = 0
        for l in f:
            if ',' in (l := l.strip()):
                draw = l.split(',')
            elif not l:
                boards.append(Board())
                y = 0
            else:
                boards[-1].numbers.update({n: (x, y) for x, n in enumerate(l.split())})
                y += 1
    return draw, boards


def simulate(draw, boards):
    first, win_sequence = None, set()
    for n in draw:
        for board in boards:
            try:
                n in board
            except Bingo as e:
                if not first:
                    first = str(e)
                win_sequence.add(board)
                if len(win_sequence) == len(boards):
                    return first, str(e)
    return '', ''


if __name__ == '__main__':
    draw, boards = parse_input('inputs/day4test.txt')
    first, last = simulate(draw, boards)
    assert '4512' in first
    assert '1924' in last

    draw, boards = parse_input('inputs/day4.txt')
    first, last = simulate(draw, boards)
    assert '50008' in first
    assert '17408' in last


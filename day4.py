import collections


class Board:

    def __init__(self):
        self.numbers = {}
        self.x_hit = collections.defaultdict(int)
        self.y_hit = collections.defaultdict(int)

    def is_bingo(self, number):
        if number in self.numbers:
            x, y = self.numbers.pop(number)
            self.x_hit[x] += 1
            self.y_hit[y] += 1
            if self.x_hit[x] == 5 or self.y_hit[y] == 5:
                return sum(map(int, self.numbers)) * int(number)

            
def parse_input(input_file):
    draw, boards = [], []
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
            if (score := board.is_bingo(n)):
                if not first:
                    first = score
                win_sequence.add(board)
                if len(win_sequence) == len(boards):
                    return first, score
    return None, None


if __name__ == '__main__':
    draw, boards = parse_input('inputs/day4test.txt')
    assert (4512, 1924) == simulate(draw, boards)

    draw, boards = parse_input('inputs/day4.txt')
    assert (50008, 17408) == simulate(draw, boards)

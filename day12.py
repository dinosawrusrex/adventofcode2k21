import collections

def map_system(connections):
    system = collections.defaultdict(list)
    for c in connections:
        start, end = c.strip().split('-')
        if end == 'start':
            start, end = end, start
        system[start].append(end)
        if end != 'end' and start != 'start':
            system[end].append(start)
    return system

def simulate_journeys(system, curr=None, path=None, small_cave_repeat=False):
    journeys = []
    curr = curr if curr else 'start'
    path = path[:] if path else []
    path.append(curr)

    if curr == 'end':
        journeys.append(path)
        return journeys

    for c in system[curr]:
        if c.islower():
            if small_cave_repeat:
                small_caves = collections.Counter(c for c in path if c.islower() and c not in ['start', 'end'])
                if 2 in small_caves.values() and c in small_caves:
                    continue
            elif c in path:
                continue
        journeys.extend(simulate_journeys(system, curr=c, path=path, small_cave_repeat=small_cave_repeat))

    return journeys


if __name__ == '__main__':
    sample = [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end',
    ]
    system = map_system(sample)
    assert len(simulate_journeys(system)) == 10
    assert len(simulate_journeys(system, small_cave_repeat=True)) == 36

    sample = [
        'dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc',
    ]

    system = map_system(sample)
    assert len(simulate_journeys(system)) == 19
    assert len(simulate_journeys(system, small_cave_repeat=True)) == 103

    sample = [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW',
    ]

    system = map_system(sample)
    assert len(simulate_journeys(system)) == 226
    assert len(simulate_journeys(system, small_cave_repeat=True)) == 3509

    connections = [
        'bm-XY',
        'ol-JS',
        'bm-im',
        'RD-ol',
        'bm-QI',
        'JS-ja',
        'im-gq',
        'end-im',
        'ja-ol',
        'JS-gq',
        'bm-AF',
        'RD-start',
        'RD-ja',
        'start-ol',
        'cj-bm',
        'start-JS',
        'AF-ol',
        'end-QI',
        'QI-gq',
        'ja-gq',
        'end-AF',
        'im-QI',
        'bm-gq',
        'ja-QI',
        'gq-RD',
    ]

    system = map_system(connections)
    assert len(simulate_journeys(system)) == 3887
    assert len(simulate_journeys(system, small_cave_repeat=True)) == 104834

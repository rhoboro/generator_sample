from random import randint

from enum import Enum


class Card(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2


def Player(name):
    yield name
    while True:
        own = Card(randint(0, 2))
        yield own


def start(p1, p2, n):
    count = 0
    count_p1 = 0
    count_p2 = 0
    p1_name = next(p1)
    p2_name = next(p2)
    print(f'{p1_name} VS {p2_name}')
    while True:
        count += 1
        print(f'#### ROUND {count} ###')
        p1x = next(p1)
        p2x = next(p2)
        result = (p1x.value - p2x.value + 3) % 3
        if result == 0:
            print(f'{p1x.name}, {p2x.name} => even')
        elif result == 1:
            count_p1 += 1
            print(f'{p1x.name}, {p2x.name} => {p1_name} +1')
        elif result == 2:
            count_p2 += 1
            print(f'{p1x.name}, {p2x.name} => {p2_name} +1')

        if max(count_p1, count_p2) < n:
            print()
            continue

        if n <= count_p1:
            print(f'{p1_name}: {count_p1} {p2_name}: {count_p2}')
            print(f'{p1_name} are winner')
            p1.close()
            p2.close()
            break
        elif n <= count_p2:
            print(f'{p1_name}: {count_p1} {p2_name}: {count_p2}')
            print(f'{p1_name} are loser')
            p1.close()
            p2.close()
            break


if __name__ == '__main__':
    taro = Player('Taro')
    hanako = Player('Hanako')
    start(taro, hanako, 3)


import random
from copy import deepcopy


class World:
    def __init__(self):
        self.world = [[] for _ in range(10)]
        self.moves_count = 0

    def generate_new_world(self):
        self.world = [[] for _ in range(10)]
        for i in range(10):
            self.world[random.randint(0, 9)].append(i)
        return self.show()

    def show(self):
        high = max([len(i) for i in self.world])
        string = "---" * 10 + '\n'
        string += "   " * 10 + '\n'
        for cur_high in range(high - 1, -1, -1):
            for i in range(10):
                if len(self.world[i]) <= cur_high:
                    string += '   '
                else:
                    string += '  ' + str(self.world[i][cur_high])
            string += '\n'
        string += "---" * 10 + '\n'
        string += '  1  2  3  4  5  6  7  8  9  10' + '\n'
        string += 'Ходы: ' + str(self.moves_count) + '\n'
        return string

    def random_move(self):
        possibles = []
        al = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(10):
            if self.world[i]:
                possibles.append(i)
        ch = random.choice(possibles)
        al.pop(ch)
        self.moves_count += 1
        self.world[random.choice(al)].append(self.world[ch].pop())
        return self.show()

    def move(self, s1, s2):
        # индексация с 1
        if self.world[s1 - 1]:
            self.moves_count += 1
            self.world[s2 - 1].append(self.world[s1 - 1].pop())
            return self.show()
        else:
            return "You are trying to move unexisting piece"

    def is_win(self):
        for i in range(10):
            if not self.world[i] or self.world[i] != [i]:
                return False
        return True

    def do_best_move(self):
        def get_board_value(b):
            v = 0
            for place in range(10):
                for block in range(len(b[place])):
                    if b[place][block] != place:
                        v += len(b[b[place][block]]) + 1
                        # v += (len(b[place]) - block - 1)
                        # if len(b[b[place][block]]) == 0 and (len(b[place]) - block - 1) == 0:
                        #     v -= 1
                    elif len(b[place]) > 1 and block != 0:
                        v += block + 2
            return v

        mn = get_board_value(self.world)
        p1 = p2 = -1
        future_placements = 0
        future_p1 = future_p2 = -1
        for place1 in range(10):
            if self.world[place1] and not (self.world[place1][-1] == place1 and len(self.world[place1]) == 1):
                for place2 in range(10):
                    if place2 != place1:
                        board = self.world
                        new_board = deepcopy(self.world)
                        new_board[place2].append(new_board[place1].pop())
                        next_val = get_board_value(new_board)
                        if next_val < mn:
                            p1 = place1
                            p2 = place2
                            mn = next_val
                        if p1 == p2 == -1:
                            #ищем сколько может встать на свое место
                            placements = 0
                            for place in range(10):
                                if new_board[place] and not (new_board[place][-1] == place and len(new_board[place]) == 1):
                                    if not new_board[new_board[place][-1]]:
                                        placements+=1
                            if future_placements < placements:
                                future_placements = placements
                                future_p1 = place1
                                future_p2 = place2
        if p1 == -1:
            p1 = future_p1
            p2 = future_p2
        string = f"Оценка текущей позиции: {mn}\n" + f'Делаем лучший ход: {p1 + 1} -> {p2 + 1}\n'
        return string + self.move(p1 + 1, p2 + 1)


def get_board_value(b):
    v = 0
    for place in range(10):
        for block in range(len(b[place])):
            if b[place][block] != place:
                v += len(b[b[place][block]]) + 1
                v += (len(b[place]) - block - 1) * 0.01
            elif len(b[place]) > 1 and block != 0:
                v += block + 2

    return v


# Запуск тестов
if __name__ == "__main__":
    world = World()
    world.world = [[3], [], [], [9], [6], [0], [8], [4], [5], [1, 2, 7]]
    print(world.show())
    while not world.is_win():
        print(world.do_best_move())


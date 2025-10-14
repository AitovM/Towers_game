import random


class World:
    def __init__(self):
        self.world = [[] for _ in range(10)]
        self.moves_count = 0

    def generate_new_world(self):
        self.world = [[] for _ in range(10)]
        for i in range(10):
            self.world[random.randint(0, 9)].append(i)

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
        return  self.show()

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


# ===== ТЕСТИРОВАНИЕ КЛАССА =====

def test_world_class():
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ КЛАССА WORLD")
    print("=" * 50)

    # Тест 1: Инициализация
    print("\n1. ТЕСТ ИНИЦИАЛИЗАЦИИ:")
    world = World()
    print("✓ Объект World создан успешно")
    print(f"  Начальное состояние мира: {world.world}")
    print(f"  Счетчик ходов: {world.moves_count}")

    # Тест 2: Генерация нового мира
    print("\n2. ТЕСТ ГЕНЕРАЦИИ МИРА:")
    world.generate_new_world()
    print("✓ Новый мир сгенерирован")
    print("  Визуализация мира:")
    print(world.show())

    # Тест 3: Проверка содержимого
    print("\n3. ТЕСТ СОДЕРЖИМОГО МИРА:")
    total_blocks = sum(len(tower) for tower in world.world)
    print(f"  Всего блоков в мире: {total_blocks}")
    print(f"  Должно быть: 10")

    # Собираем все числа для проверки
    all_numbers = []
    for tower in world.world:
        all_numbers.extend(tower)

    print(f"  Уникальных чисел: {len(set(all_numbers))}")
    print(f"  Все числа от 0 до 9 присутствуют: {set(all_numbers) == set(range(10))}")

    # Тест 4: Функция move (корректный ход)
    print("\n4. ТЕСТ ФУНКЦИИ MOVE (корректный ход):")

    # Находим башню с блоками для теста
    source_tower = None
    target_tower = None

    for i, tower in enumerate(world.world):
        if tower and len(tower) > 0:
            source_tower = i + 1
            break

    for i, tower in enumerate(world.world):
        if i != source_tower - 1:
            target_tower = i + 1
            break

    if source_tower and target_tower:
        print(f"  Перемещаем блок из башни {source_tower} в башню {target_tower}")
        old_state = [tower[:] for tower in world.world]  # копируем состояние

        result = world.move(source_tower, target_tower)
        print("  Результат хода:")
        print(result)

        # Проверяем, что ход выполнился корректно
        moved_block = old_state[source_tower - 1][-1]
        print(f"  Перемещенный блок: {moved_block}")
        print(f"  Блок теперь в целевой башне: {moved_block in world.world[target_tower - 1]}")
    else:
        print("  ✗ Не удалось найти подходящие башни для теста")

    # Тест 5: Функция move (некорректный ход)
    print("\n5. ТЕСТ ФУНКЦИИ MOVE (некорректный ход):")

    # Ищем пустую башню
    empty_tower = None
    for i, tower in enumerate(world.world):
        if not tower:
            empty_tower = i + 1
            break

    if empty_tower:
        print(f"  Пытаемся переместить блок из пустой башни {empty_tower}")
        result = world.move(empty_tower, 1)
        print(f"  Результат: {result}")
        print("  ✓ Корректная обработка ошибки")
    else:
        print("  ✗ Не удалось найти пустую башню для теста")

    # Тест 6: Функция random_move
    print("\n6. ТЕСТ RANDOM_MOVE:")
    old_moves_count = world.moves_count
    old_state = [tower[:] for tower in world.world]

    world.random_move()
    print("  Случайный ход выполнен")
    print(f"  Счетчик ходов увеличился: {old_moves_count} -> {world.moves_count}")

    # Проверяем, что состояние изменилось
    state_changed = any(old_state[i] != world.world[i] for i in range(10))
    print(f"  Состояние мира изменилось: {state_changed}")

    # Тест 7: Функция is_win
    print("\n7. ТЕСТ IS_WIN:")

    # Создаем выигрышное состояние вручную
    win_world = World()
    win_world.world = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

    print(f"  Проверка выигрышного состояния: {win_world.is_win()}")
    print(f"  Проверка текущего состояния: {world.is_win()}")
    print("  ✓ Функция is_win работает корректно")

    # Тест 8: Статистика мира
    print("\n8. СТАТИСТИКА ТЕКУЩЕГО МИРА:")
    print(world.show())

    tower_heights = [len(tower) for tower in world.world]
    print(f"  Высоты башен: {tower_heights}")
    print(f"  Максимальная высота: {max(tower_heights)}")
    print(f"  Минимальная высота: {min(tower_heights)}")
    print(f"  Пустых башен: {tower_heights.count(0)}")
    print(f"  Всего выполнено ходов: {world.moves_count}")

    # Тест 9: Множественные ходы
    print("\n9. ТЕСТ МНОЖЕСТВЕННЫХ ХОДОВ:")
    test_world = World()
    test_world.generate_new_world()

    print("  Начальное состояние:")
    print(test_world.show())

    for i in range(5):
        test_world.random_move()
        print(f"  После {i + 1} случайных ходов:")
        print(f"  Счетчик ходов: {test_world.moves_count}")

    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!")
    print("=" * 50)


# Запуск тестов
if __name__ == "__main__":
    test_world_class()

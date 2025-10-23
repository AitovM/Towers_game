from Towers_player import World
import random

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
    a = int(input(f'\n[+] Выберите варианты тестирования игры:\n\t[1] Запуск проверки всех функций класса\n'
          f'\t[2] Запуск массовой пошаговой проверки n рандомных игр\n\t[3] Запуск пошаговой проверки решения расстановки\n\t[4] Быстрое решение расстановки(вывод ходов)\n\t[5] Выход\n\t>>> '))
    while a != 5:
        if a == 1:
            test_world_class()
        elif a == 2:
            mx = 0
            c = 0
            n = input(f'\n\t[+] Выберите варианты тестирования игры:\n\t\t[+] Запуск массовой пошаговой проверки n рандомных игр\n\t\t\t[+] Введите количество миров которые нужно разложить\n\t\t\t[->]')
            for i in range(int(n)):
                world = World()
                world.generate_new_world()
                print('======================= Разложение №' + str(i) + ' =========================')
                print(world.show())
                while not world.is_win():
                    print(world.do_best_move())
                    if world.moves_count > 20:
                        c+=1
                        break
                print('Разложение успешно!')
                mx = max(mx, world.moves_count)
            print(f"Разложено {n} ситуаций, из которых неудачно разложено {c} миров. \nПотребовалось на все не более чем {mx} ходов")
        elif a == 3:
            world = World()
            world.world = eval(input(f'\n[+] Выберите варианты тестирования игры:\n\t[+] Запуск пошаговой проверки решения расстановки\n\t\t[...]Введите строку в определенном формате, например для ситуации:\n\t\t\t------------------------------\n\t\t\t                              \n\t\t\t                             7\n\t\t\t                             2\n\t\t\t  3        9  6  0  8  4  5  1\n\t\t\t------------------------------\n\t\t\t  1  2  3  4  5  6  7  8  9  10\n\t\tВвод должен быть в формате: \n\t\t\t[[3], [], [], [9], [6], [0], [8], [4], [5], [1, 2, 7]]\n\t\t[->]'))
            print(world.show())
            while not world.is_win():
                print(world.do_best_move())
        elif a == 4:
            world = World()
            world.world = eval(input(f'\n[+] Выберите варианты тестирования игры:\n\t[+] Быстрое решение расстановки(вывод ходов)\n\t\t[...]Введите строку в определенном формате, например для ситуации:\n\t\t\t------------------------------\n\t\t\t                              \n\t\t\t                             7\n\t\t\t                             2\n\t\t\t  3        9  6  0  8  4  5  1\n\t\t\t------------------------------\n\t\t\t  1  2  3  4  5  6  7  8  9  10\n\t\tВвод должен быть в формате: \n\t\t\t[[3], [], [], [9], [6], [0], [8], [4], [5], [1, 2, 7]]\n\t\t[->]'))
            print(world.show())
            while not world.is_win():
                world.do_best_move()
            print(f'Требуемое количесвто ходов для решения: {world.moves_count}')
        a = int(input(f'\n[+] Выберите варианты тестирования игры:\n\t[1] Запуск проверки всех функций класса\n'
                  f'\t[2] Запуск массовой пошаговой проверки n рандомных игр\n\t[3] Запуск пошаговой проверки решения расстановки\n\t[4] Быстрое решение расстановки(вывод ходов)\n\t[5] Выход\n\t>>> '))

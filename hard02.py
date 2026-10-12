""" Задание 2. Поиск выхода из лабиринта """
from collections import deque

def find_path(maze):
    """ Обход в ширину """
    rows = len(maze)
    cols = len(maze[0])

    start = None
    finish = None

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == "S":
                start = (row, col)
            elif maze[row][col] == "F":
                finish = (row, col)

    if start is None or finish is None:
        raise ValueError("В лабиринте должны быть S и F")

    queue = deque([start])

    parents = {start: None}

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    while queue:
        current = queue.popleft()

        if current == finish:
            path = []

            while current is not None:
                path.append(current)
                current = parents[current]

            path.reverse()
            return path

        row, col = current

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc
            neighbor = (next_row, next_col)

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and maze[next_row][next_col] != 1
                and neighbor not in parents
            ):
                parents[neighbor] = current
                queue.append(neighbor)

    return None

def main():
    """ Основная функция для поиска выходв из лабиринта """

    maze = [
        ["S",  0,  0,  1 ],
        [ 1,   0,  0,  0 ],
        [ 1,   0,  1,  0 ],
        [ 1,   1,  0, "F"],
    ]

    path = find_path(maze)

    if path is None:
        print("Путь не найден!")
    else:
        print(f"Путь найден! Длина пути: {len(path) - 1}")
        print("Маршрут:", " -> ".join(f"({r},{c})" for r, c in path))

if __name__ == '__main__':
    main()

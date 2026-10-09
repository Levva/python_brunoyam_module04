""" Задание 2. Поиск выхода из лабиринта """
from collections import deque

def bfs(maze):
    """ Обход в ширину """
    visited = set()
    queue = deque([maze])
    start = []
    visited.add(start)
    while queue:
        folder = queue.popleft()
        real_folder = folder.resolve()
        if real_folder in visited:
            continue
        visited.add(real_folder)
        print(folder)
        for child in folder.iterdir():
            if child.is_dir():
                queue.append(child)

def main():
    """ Основная функция для поиска выходв из лабиринта """

    maze = [
        ["S", 0,  0,  1],
        [1,  0,  0,  0],
        [1,  0,  1,  0],
        [1,  1,  0, "F"]
    ]

    bfs(maze)

if __name__ == '__main__':
    main()

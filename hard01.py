""" Задание 1. Обход папок """
from collections import deque
from pathlib import Path

def dfs(start):
    """ Обход в глубину """
    founded = set()
    stack = [Path(start)]
    print(f"Обход директории {start} в глубину:")
    while stack:
        folder = stack.pop()
        real_folder = folder.resolve()
        if real_folder in founded:
            continue
        founded.add(real_folder)
        print(folder)
        try:
            for child in folder.iterdir():
                if child.is_dir():
                    stack.append(child)
        except PermissionError:
            print(f"Нет доступа: {folder}")

def bfs(start):
    """ Обход в ширину """
    founded = set()
    queue = deque([Path(start)])
    print(f"Обход директории {start} в ширину:")
    while queue:
        folder = queue.popleft()
        real_folder = folder.resolve()
        if real_folder in founded:
            continue
        founded.add(real_folder)
        print(folder)
        try:
            for child in folder.iterdir():
                if child.is_dir():
                    queue.append(child)
        except PermissionError:
            print(f"Нет доступа: {folder}")

def main():
    """ Основная функция для обхода по всем файлам и папкам в указанной директории """
    start = "./"

    dfs(start)
    bfs(start)

if __name__ == '__main__':
    main()

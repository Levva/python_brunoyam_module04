"""Задание 1. Очередь заказов"""
from collections import deque

def process_orders(orders_deque):
    """ Обрабатывает заказы"""
    while orders_deque:
        order = orders_deque.popleft()
        print(f"Заказ {order} обработан!")

def main():
    """ Основная функция для очереди заказов """
    orders = deque()
    orders.append("Капучино")
    orders.append("Kpyассан")
    orders.append("Латте")
    orders.append("Паштейш")

    print(f"Заказов в очереди: {len(orders)}")
    process_orders(orders)
    print(f"Осталось обработать заказов: {len(orders)}")
if __name__ == '__main__':
    main()

import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor

# 单进程多线程生成任务
from tasks_schedule.producer.node import Node
from tasks_schedule.producer.scene import Scene
from tasks_schedule.producer.task import TaskFactory


def schedule_create_task(node):
    # task = TaskFactory.create_task(Node(symbol))
    print("schedule_create_task")


def create_task(symbol):
    #  创建任务
    node = Node(symbol)
    Scene.main_loop(schedule_create_task, node)


symbols = ['BTC/USDT', 'BTC/USDS']


def create_server():
    thread_size = len(symbols)
    pool = ThreadPoolExecutor(thread_size)
    for symbol in symbols:
        pool.submit(create_task, symbol)


if __name__ == '__main__':
    create_server()

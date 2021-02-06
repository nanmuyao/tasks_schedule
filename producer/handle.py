import os
import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor

from producer.node import Node
from producer.scene import Scene
from producer.task import TaskFactory


def on_loop(var):
    run_duration = random.randint(2, 4)
    print(f'on_loop start, {var} sleep {run_duration}')
    time.sleep(10)


def create_task(symbol):
    #  创建任务
    node = Node(symbol)
    Scene.main_loop(on_loop, node)


symbols = ['BTC/USDT', 'BTC/USDS']


def create_server():
    thread_size = len(symbols)
    thread_size = 1
    pool = ThreadPoolExecutor(thread_size)
    for symbol in symbols:
        pool.submit(create_task, symbol)


if __name__ == '__main__':
    create_server()

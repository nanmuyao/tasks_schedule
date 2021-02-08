import os
import sys
import time
import threading
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from tasks_schedule.producer.node import Node
from tasks_schedule.producer.scene import Scene


def on_loop(var):
    run_duration = random.randint(1, 5)
    if run_duration > 3:
        raise Exception("test exit")
    time.sleep(run_duration)


def create_task(symbol):
    #  创建任务
    node = Node(symbol)
    Scene.main_loop(on_loop, node)


symbols = ['BTC/USDT', 'BTC/USDS']


def inspect_thread_position(thread):
    frame = sys._current_frames().get(thread.ident, None)
    if frame:
        print("inspect thread positon", frame.f_code.co_filename, frame.f_code.co_name, frame.f_code.co_firstlineno)


def create_server_thread_pool():
    thread_size = len(symbols)
    threading.TIMEOUT_MAX = 1
    pool = ThreadPoolExecutor(thread_size)
    for symbol in symbols:
        pool.submit(create_task, symbol)

    while True:
        print("main thread heart beat")
        threads = threading.enumerate()
        task_node = []
        for thread in threads:
            name = thread.getName()
            if ":" in name:
                threadid, node = thread.getName().split(":")
                print(f"task node {node}")
                task_node.append(node)
                inspect_thread_position(thread)

        # 监控任务，如果任务down掉，然后再重启，尝试失败
        # difference_nodes = set(symbols).difference(task_node)
        # if difference_nodes:
        #     print(f'task down {difference_nodes}')
        #     for node in difference_nodes:
        #         pool.submit(create_task, node)
        time.sleep(3)


def inspect_thread():
    print("inspect thread")
    while True:
        threads = threading.enumerate()
        print(f'threads cnt===={len(threads)}')
        running_symbol = []
        for thread in threads:
            name = thread.getName()
            if ":" in name:
                thread_id, node = name.split(":")
                running_symbol.append(node)
                print(thread_id, node)
        need_create_thread_symbols = list(set(symbols).difference(running_symbol))
        for symbol in need_create_thread_symbols:
            create_thread(symbol)
        time.sleep(4)


def create_thread(symbol):
    t = Thread(target=create_task, args=(symbol,))
    t.start()


def create_server():
    for symbol in symbols:
        create_thread(symbol)

    inspect = Thread(target=inspect_thread, args=())
    inspect.start()


if __name__ == '__main__':
    create_server()
# create_server_thread_pool()

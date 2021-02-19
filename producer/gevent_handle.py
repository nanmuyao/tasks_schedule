import sys
import gevent
import time
import threading
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from gevent import monkey

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


def create_server():
    for symbol in symbols:
        pass


if __name__ == '__main__':
    monkey.patch_all()


    def foo():
        print('Running in foo')
        gevent.sleep(0)
        print('Explicit context switch to foo again')


    def bar():
        print('Explicit context to bar')
        gevent.sleep(0)
        print('Implicit context switch back to bar')


    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])

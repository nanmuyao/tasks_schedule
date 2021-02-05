import threading
import os
import time

from tasks_schedule.common.lib_wrap.meta_class import MetaClass
from tasks_schedule.producer.task import TaskFactory


class Scene(MetaClass):
    def __init__(self):
        pass

    @classmethod
    def main_loop(cls, on_loop, node):
        while True:
            print(
                f'create_task pid {os.getpid()}, '
                f'tid {threading.get_ident()}, '
                f'args {node}, '
            )
            on_loop(node)
            time.sleep(1)

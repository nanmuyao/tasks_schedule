import threading
import os
import time

from func_timeout import func_timeout, FunctionTimedOut

from common.lib_wrap.meta_class import MetaClass
from producer.task import TaskFactory


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
            try:
                func_timeout(3, on_loop, (node,))
            except Exception as timeout_exception:
                # 这里想捕获超时的异常，暂时不能捕获
                print(f"loop exception, eeeeeeeeeeeeeeeeeee{e}")
            time.sleep(1)

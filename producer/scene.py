import threading
import os
import time

from tasks_schedule.common.lib_wrap.meta_class import MetaClass


class Scene(MetaClass):
    def __init__(self):
        pass

    @classmethod
    def main_loop(cls, on_loop, node):
        thread = threading.current_thread()
        thread.setName(f"{threading.get_ident()}:{node.symbol}")
        while True:
            # print(
            #     f'create_task pid {os.getpid()}, '
            #     f'tid {threading.get_ident()}, '
            #     f'args {node}, '
            # )
            try:
                on_loop(node)
            except Exception as e:
                print(f'on_loop exception ======================= {e}')
                raise e
            time.sleep(1)

    def monitor_task(self):
        pass

from tasks_schedule.common.lib_wrap.meta_class import MetaClass
from .task import Task, TaskFactory


class Layer(MetaClass):
    pass


class ProducerRateLayer(Layer):
    # 控制生产速率
    def __init__(self):
        pass

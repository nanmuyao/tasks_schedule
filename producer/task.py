from tasks_schedule.common.lib_wrap.meta_class import MetaClass


class Task(MetaClass):
    @classmethod
    def create_task(cls, node):
        print("Task create task")


class TaskFactory(MetaClass):
    @classmethod
    def create_task(cls, node):
        return Task.create_task(node)

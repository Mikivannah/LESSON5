# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть
# атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False  # По умолчанию задача не выполнена

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, task_index):
        self.tasks[task_index].status = True

    def list_tasks(self):
        print("Список текущих задач:")
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f"{i+1}. {task.description} (Срок выполнения: {task.due_date})")

# Пример использования
task_manager = TaskManager()

task1 = Task("Подготовить отчет", "01.05.2024")
task2 = Task("Созвониться с партнером", "03.05.2024")
task3 = Task("Сдать домашнее задание", "05.05.2024")

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.mark_task_as_done(0)

task_manager.list_tasks()
# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть
# атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Выполнено"

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "Не выполнено"]
        return current_tasks

# Пример использования
task_manager = TaskManager()


task_manager.add_task("Сделать уроки", "10.03.2024")
task_manager.add_task("Сходить в магазин", "15.03.2024")
task_manager.add_task("Позвонить другу", "15.03.2024")
task_manager.add_task("Прочитать статью", "10.03.2024")
task_manager.add_task("Написать код", "15.03.2024")
task_manager.add_task("Позвонить другу", "15.03.2024")

task_manager.mark_as_done("Позвонить другу")
task_manager.mark_as_done("Сделать уроки")

current_tasks = task_manager.get_current_tasks()
for task in current_tasks:
    print("Осталось сделать:", task.description, task.deadline)
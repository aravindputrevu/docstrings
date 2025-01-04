from typing import List, Dict

class Task:
    def __init__(self, title: str, description: str, status: str = "Pending"):
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self) -> None:
        self.status = "Completed"

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.status == "Pending"]

class TaskManagementSystem:
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(self, project_name: str) -> None:
        self.projects[project_name] = Project(project_name)

    def add_task_to_project(self, project_name: str, task: Task) -> None:
        if project_name in self.projects:
            self.projects[project_name].add_task(task)
        else:
            raise ValueError("Project not found")

    def get_all_pending_tasks(self) -> List[Task]:
        pending_tasks = []
        for project in self.projects.values():
            pending_tasks.extend(project.get_pending_tasks())
        return pending_tasks

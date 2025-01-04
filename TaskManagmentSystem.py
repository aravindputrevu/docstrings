from typing import List, Dict

class Task:
    def __init__(self, title: str, description: str, status: str = "Pending"):
        """
        Initialize a new Task with specified details.
        
        Parameters:
            title (str): The title or name of the task
            description (str): A detailed description of the task
            status (str, optional): Current status of the task. Defaults to "Pending"
        
        Attributes:
            title (str): Stores the task's title
            description (str): Stores the task's description
            status (str): Tracks the current state of the task
        """
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self) -> None:
        """
        Mark the current task as completed by updating its status.
        
        This method changes the task's status from its current state to "Completed", 
        indicating that the task has been finished or resolved.
        
        Returns:
            None: The method modifies the task's status in-place without returning a value.
        """
        self.status = "Completed"

class Project:
    def __init__(self, name: str):
        """
        Initialize a new Project instance.
        
        Parameters:
            name (str): The name of the project.
        
        Attributes:
            name (str): The project's unique identifier.
            tasks (List[Task]): A list to store tasks associated with this project, initially empty.
        """
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Add a task to the project's task list.
        
        Parameters:
            task (Task): The task to be added to the project's collection of tasks.
        
        Returns:
            None
        """
        self.tasks.append(task)

    def get_pending_tasks(self) -> List[Task]:
        """
        Retrieve all pending tasks in the project.
        
        Returns:
            List[Task]: A list of tasks that have not yet been completed, 
                        filtered by their 'Pending' status.
        """
        return [task for task in self.tasks if task.status == "Pending"]

class TaskManagementSystem:
    def __init__(self):
        """
        Initialize an empty dictionary to store projects in the task management system.
        
        The projects dictionary uses project names as keys and Project objects as values,
        allowing for efficient project management and retrieval.
        
        Returns:
            None
        """
        self.projects: Dict[str, Project] = {}

    def create_project(self, project_name: str) -> None:
        """
        Create a new project in the task management system.
        
        Parameters:
            project_name (str): The name of the project to be created.
        
        Raises:
            None
        
        Returns:
            None
        
        Description:
            Instantiates a new Project object with the given project name and adds it 
            to the projects dictionary, using the project name as the key. If a project 
            with the same name already exists, it will be overwritten.
        """
        self.projects[project_name] = Project(project_name)

    def add_task_to_project(self, project_name: str, task: Task) -> None:
        """
        Add a task to a specified project in the task management system.
        
        Parameters:
            project_name (str): The name of the project to which the task will be added.
            task (Task): The task object to be added to the project.
        
        Raises:
            ValueError: If the specified project does not exist in the task management system.
        
        Example:
            system = TaskManagementSystem()
            system.create_project("Development")
            new_task = Task("Implement feature", "Add new user authentication")
            system.add_task_to_project("Development", new_task)
        """
        if project_name in self.projects:
            self.projects[project_name].add_task(task)
        else:
            raise ValueError("Project not found")

    def get_all_pending_tasks(self) -> List[Task]:
        """
        Retrieve all pending tasks across all projects in the task management system.
        
        Returns:
            List[Task]: A list of all tasks with 'Pending' status from all projects.
        
        Example:
            task_system = TaskManagementSystem()
            task_system.create_project('Development')
            task_system.create_project('Marketing')
            task_system.add_task_to_project('Development', Task('Code Review', 'Review pull requests'))
            task_system.add_task_to_project('Marketing', Task('Campaign Planning', 'Plan Q2 marketing strategy'))
            pending_tasks = task_system.get_all_pending_tasks()  # Returns list of pending tasks
        """
        pending_tasks = []
        for project in self.projects.values():
            pending_tasks.extend(project.get_pending_tasks())
        return pending_tasks

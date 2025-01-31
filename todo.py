#!/usr/bin/env python3
import sqlite3
import argparse
import sys

DB_NAME = "todo.db"

def init_db():
    """Initialize the SQLite database and create the todos table if needed."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task):
    """Add a new task to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    print(f"Task added with id: {cursor.lastrowid}")
    conn.close()

def list_tasks():
    """List all tasks from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, completed, created_at FROM todos ORDER BY id")
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found.")
    else:
        for row in rows:
            task_id, task, completed, created_at = row
            status = "✓" if completed else " "
            print(f"[{task_id}] [{status}] {task} (Created: {created_at})")
    conn.close()

def delete_task(task_id):
    """Delete a task by its id."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        print(f"No task found with id: {task_id}")
    else:
        conn.commit()
        print("Task deleted.")
    conn.close()

def update_task(task_id, new_task):
    """Update the task description for a given task id."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET task = ? WHERE id = ?", (new_task, task_id))
    if cursor.rowcount == 0:
        print(f"No task found with id: {task_id}")
    else:
        conn.commit()
        print("Task updated.")
    conn.close()

def mark_complete(task_id, complete=True):
    """Mark a task as complete or incomplete."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET completed = ? WHERE id = ?", (1 if complete else 0, task_id))
    if cursor.rowcount == 0:
        print(f"No task found with id: {task_id}")
    else:
        conn.commit()
        state = "completed" if complete else "incomplete"
        print(f"Task marked as {state}.")
    conn.close()

def main():
    # Set up argument parsing with subcommands for each action.
    parser = argparse.ArgumentParser(description="Todo List App using SQLite")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Command to add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task", type=str, help="Task description")
    
    # Command to list all tasks
    subparsers.add_parser("list", help="List all tasks")
    
    # Command to delete a task by id
    parser_delete = subparsers.add_parser("delete", help="Delete a task by id")
    parser_delete.add_argument("id", type=int, help="Task id")
    
    # Command to update a task
    parser_update = subparsers.add_parser("update", help="Update a task by id")
    parser_update.add_argument("id", type=int, help="Task id")
    parser_update.add_argument("task", type=str, help="New task description")
    
    # Command to mark a task as complete
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("id", type=int, help="Task id")
    
    # Command to mark a task as incomplete
    parser_incomplete = subparsers.add_parser("incomplete", help="Mark a task as incomplete")
    parser_incomplete.add_argument("id", type=int, help="Task id")
    
    args = parser.parse_args()

    # Initialize the database (creates it on first run)
    init_db()
    
    # Execute the requested command
    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "update":
        update_task(args.id, args.task)
    elif args.command == "complete":
        mark_complete(args.id, True)
    elif args.command == "incomplete":
        mark_complete(args.id, False)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
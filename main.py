import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
supabase = create_client(url, key)

def list_tasks():
    response = supabase.table('tasks').select('*').order('id').execute()
    tasks = response.data
    print("\n----- Your Tasks -----")
    if not tasks:
        print("  No tasks yet!")
    for task in tasks:
        mark = "x" if task['is_done'] else " "
        print(f"  #{task['id']}  [{mark}]  {task['title']}")

def complete_task():
    list_tasks()
    task_id = input("Enter the ID of the task to mark as done: ")
    supabase.table('tasks').update({'is_done': True}).eq('id', task_id).execute()
    print("Task marked as done!")


def delete_task():
    list_tasks()
    task_id = input("Enter the ID of the task to delete: ")
    supabase.table('tasks').delete().eq('id', task_id).execute()
    print("Task deleted!")

def add_task():
    title = input("Task title: ")
    supabase.table('tasks').insert({'title': title}).execute()
    print("Task added!")

def show_menu():
    print("\n===== My Task Tracker =====")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


main()
import os
from cli.handlers import (
    handle_register,
    handle_login,
    handle_create_task,
    handle_list_tasks,
    handle_update_task,
    handle_delete_task,
    handle_view_profile,
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("   Task Management System")
        print("=" * 40)
        print("  1. Login")
        print("  2. Register")
        print("  3. Exit")
        print("=" * 40)

        choice = input("Choose: ").strip()

        if choice == "1":
            handle_login()
        elif choice == "2":
            handle_register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to continue...")


def task_menu(token):
    while True:
        clear_screen()
        print("=" * 40)
        print("   My Tasks")
        print("=" * 40)
        print("  1. View All Tasks")
        print("  2. Create Task")
        print("  3. Update Task")
        print("  4. Delete Task")
        print("  5. View Profile")
        print("  6. Logout")
        print("=" * 40)

        choice = input("Choose: ").strip()

        if choice == "1":
            handle_list_tasks(token)
        elif choice == "2":
            handle_create_task(token)
        elif choice == "3":
            handle_update_task(token)
        elif choice == "4":
            handle_delete_task(token)
        elif choice == "5":
            handle_view_profile(token)
        elif choice == "6":
            print("Logged out!")
            break
        else:
            input("Invalid choice. Press Enter to continue...")
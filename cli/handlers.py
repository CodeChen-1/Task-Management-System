import requests

BASE_URL = "http://127.0.0.1:8000"

def handle_register():
    print("\n--- Register ---")
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    response = requests.post(f"{BASE_URL}/register", json={
        "username": username,
        "email": email,
        "password": password
    })

    if response.status_code == 200:
        print("Registration successful! You can now login.")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    response = requests.post(f"{BASE_URL}/login", json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
        token = response.json().get("access_token")
        print("Login successful!")
        from cli.menus import task_menu
        task_menu(token)
    else:
        print(f"Error: {response.json().get('detail', 'Invalid credentials')}")

    input("Press Enter to continue...")

def handle_list_tasks(token):
    print("\n--- My Tasks ---")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/tasks", headers=headers)

    if response.status_code == 200:
        tasks = response.json()
        if not tasks:
            print("No tasks yet!")
        else:
            for task in tasks:
                print(f"  [{task['id']}] {task['title']} - {task['status']} ({task['priority']})")
    else:
        print("Error fetching tasks")

    input("\nPress Enter to continue...")


def handle_create_task(token):
    print("\n--- Create Task ---")
    title = input("Title: ").strip()
    description = input("Description (optional): ").strip()
    priority = input("Priority (low/medium/high) [medium]: ").strip() or "medium"

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/tasks", headers=headers, json={
        "title": title,
        "description": description if description else None,
        "priority": priority
    })

    if response.status_code == 200:
        print("Task created!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_update_task(token):
    print("\n--- Update Task ---")
    task_id = input("Task ID: ").strip()
    title = input("New title (leave empty to skip): ").strip()
    status = input("New status (pending/in_progress/completed) (leave empty to skip): ").strip()

    headers = {"Authorization": f"Bearer {token}"}
    update_data = {}
    if title:
        update_data["title"] = title
    if status:
        update_data["status"] = status

    if not update_data:
        print("Nothing to update!")
        input("Press Enter to continue...")
        return

    response = requests.put(f"{BASE_URL}/tasks/{task_id}", headers=headers, json=update_data)

    if response.status_code == 200:
        print("Task updated!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_delete_task(token):
    print("\n--- Delete Task ---")
    task_id = input("Task ID: ").strip()
    confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip()

    if confirm.lower() != 'y':
        print("Cancelled.")
        input("Press Enter to continue...")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}", headers=headers)

    if response.status_code == 200:
        print("Task deleted!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")

def handle_view_profile(token):
    print("\n--- My Profile ---")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/me", headers=headers)

    if response.status_code == 200:
        user = response.json()
        print(f"  Username: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  Member since: {user['created_at']}")
    else:
        print("Error fetching profile")

    input("\nPress Enter to continue...")

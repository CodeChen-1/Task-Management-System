# Import the 'requests' library - this lets us send HTTP requests to our FastAPI server
import requests

# The address where our FastAPI server is running
# This is the default address uvicorn uses when you run: uvicorn app.main:app
BASE_URL = "http://127.0.0.1:8000"


def handle_register():
    """Register a new user account"""
    # Print a header so the user knows what section they're in
    print("\n--- Register ---")

    # Get user input - strip() removes extra spaces before/after
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    # Send a POST request to our API's /register endpoint
    # json= sends the data as JSON (the format FastAPI expects)
    # This is like filling out a form and submitting it
    response = requests.post(f"{BASE_URL}/register", json={
        "username": username,
        "email": email,
        "password": password
    })

    # Check if registration was successful
    # HTTP status code 200 means "OK" (success)
    if response.status_code == 200:
        print("Registration successful! You can now login.")
    else:
        # If something went wrong, get the error message from the response
        # .get('detail') looks for the 'detail' key in the JSON response
        # 'Unknown error' is the fallback if 'detail' doesn't exist
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    # Pause so user can read the message before menu reappears
    input("Press Enter to continue...")


def handle_login():
    """Login and get authentication token"""
    print("\n--- Login ---")

    # Get login credentials from user
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    # Send POST request to /login endpoint
    # This is like clicking "Login" on a website
    response = requests.post(f"{BASE_URL}/login", json={
        "username": username,
        "password": password
    })

    # Check if login was successful
    if response.status_code == 200:
        # Extract the JWT token from the response
        # The token looks like: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        # This token proves we are who we say we are
        token = response.json().get("access_token")
        print("Login successful!")

        # Import here to avoid circular imports (circular = file A imports B, B imports A)
        from cli.menus import task_menu

        # Enter the task menu, passing the token
        # The token will be used for all future requests to prove identity
        task_menu(token)
    else:
        # Login failed - show error message
        print(f"Error: {response.json().get('detail', 'Invalid credentials')}")

    input("Press Enter to continue...")


def handle_list_tasks(token):
    """List all tasks for the current user"""
    print("\n--- My Tasks ---")

    # Create the authorization header
    # This tells the server "I am user X, here is my proof (token)"
    # The format must be: "Bearer <token>" - this is a standard format
    headers = {"Authorization": f"Bearer {token}"}

    # Send GET request to /tasks endpoint
    # GET = "give me data" (as opposed to POST which means "here is data")
    # headers= passes the authorization token
    response = requests.get(f"{BASE_URL}/tasks", headers=headers)

    if response.status_code == 200:
        # response.json() converts the JSON text into a Python list of dictionaries
        # Example: [{"id": 1, "title": "Buy groceries", "status": "pending", ...}, ...]
        tasks = response.json()

        if not tasks:
            # Empty list = no tasks yet
            print("No tasks yet!")
        else:
            # Loop through each task and display it
            for task in tasks:
                # task['id'] = the task's unique number
                # task['title'] = the task's name
                # task['status'] = pending/in_progress/completed
                # task['priority'] = low/medium/high
                print(f"  [{task['id']}] {task['title']} - {task['status']} ({task['priority']})")
    else:
        print("Error fetching tasks")

    input("\nPress Enter to continue...")


def handle_create_task(token):
    """Create a new task"""
    print("\n--- Create Task ---")

    # Get task details from user
    title = input("Title: ").strip()
    description = input("Description (optional): ").strip()

    # Get priority with a default value
    # The "or" means: if user types nothing, use "medium"
    # Example: user presses Enter → priority = "" → "" or "medium" → "medium"
    priority = input("Priority (low/medium/high) [medium]: ").strip() or "medium"

    # Prepare the authorization header
    headers = {"Authorization": f"Bearer {token}"}

    # Build the task data dictionary
    # Only include description if user provided one
    task_data = {
        "title": title,
        "priority": priority
    }
    if description:
        task_data["description"] = description

    # Send POST request to create the task
    # POST = "here is new data, please create it"
    response = requests.post(f"{BASE_URL}/tasks", headers=headers, json=task_data)

    if response.status_code == 200:
        print("Task created!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_update_task(token):
    """Update an existing task"""
    print("\n--- Update Task ---")

    # Get which task to update
    task_id = input("Task ID: ").strip()

    # Get new values (user can leave empty to keep current values)
    title = input("New title (leave empty to skip): ").strip()
    status = input("New status (pending/in_progress/completed) (leave empty to skip): ").strip()

    # Prepare authorization header
    headers = {"Authorization": f"Bearer {token}"}

    # Build update data - only include fields user provided
    # This way we don't overwrite existing data with empty values
    update_data = {}
    if title:
        update_data["title"] = title
    if status:
        update_data["status"] = status

    # If user didn't provide anything to update, exit early
    if not update_data:
        print("Nothing to update!")
        input("Press Enter to continue...")
        return

    # Send PUT request to update the task
    # PUT = "here is updated data for this specific resource"
    # /tasks/{task_id} = the specific task we want to update
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", headers=headers, json=update_data)

    if response.status_code == 200:
        print("Task updated!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_delete_task(token):
    """Delete a task"""
    print("\n--- Delete Task ---")

    # Get which task to delete
    task_id = input("Task ID: ").strip()

    # Ask for confirmation before deleting
    # This is a safety measure - deleting is permanent!
    confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip()

    # If user didn't say "y" (yes), cancel the deletion
    if confirm.lower() != 'y':
        print("Cancelled.")
        input("Press Enter to continue...")
        return

    # Prepare authorization header
    headers = {"Authorization": f"Bearer {token}"}

    # Send DELETE request to remove the task
    # DELETE = "please remove this resource"
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}", headers=headers)

    if response.status_code == 200:
        print("Task deleted!")
    else:
        print(f"Error: {response.json().get('detail', 'Unknown error')}")

    input("Press Enter to continue...")


def handle_view_profile(token):
    """View current user's profile"""
    print("\n--- My Profile ---")

    # Prepare authorization header
    headers = {"Authorization": f"Bearer {token}"}

    # Send GET request to /me endpoint
    # /me = "tell me about the current user" (identified by the token)
    response = requests.get(f"{BASE_URL}/me", headers=headers)

    if response.status_code == 200:
        # Get user data from response
        user = response.json()
        # Display profile information
        print(f"  Username: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  Member since: {user['created_at']}")
    else:
        print("Error fetching profile")

    input("\nPress Enter to continue...")

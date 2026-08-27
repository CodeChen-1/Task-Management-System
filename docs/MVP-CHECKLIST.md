# MVP Checklist (Minimum Viable Product)

## What is MVP?

MVP is the simplest version of the app that works end-to-end. It includes only the essential features needed for users to complete their core tasks.

---

## MVP Features

### 1. User Authentication

| Feature | Status | Notes |
|---------|--------|-------|
| User registration | [ ] | Username, email, password |
| User login | [ ] | Username/email + password |
| User logout | [ ] | Clear session/token |
| View profile | [ ] | Show current user info |
| Password hashing | [ ] | Never store plain text passwords |
| JWT tokens | [ ] | Stateless authentication |

---

### 2. Task Management (CRUD)

| Feature | Status | Notes |
|---------|--------|-------|
| Create task | [ ] | Title, description, priority, deadline |
| View all tasks | [ ] | List user's tasks |
| View single task | [ ] | Show task details |
| Update task | [ ] | Edit any task field |
| Delete task | [ ] | Remove task permanently |
| Mark as completed | [ ] | Change status to completed |

---

### 3. Task Properties

| Property | Type | Default | Options |
|----------|------|---------|---------|
| title | string | required | 1-100 characters |
| description | text | optional | Max 1000 characters |
| status | string | pending | pending, in_progress, completed |
| priority | string | medium | low, medium, high |
| deadline | datetime | optional | Future date |
| created_at | datetime | auto | Timestamp |
| updated_at | datetime | auto | Timestamp |

---

### 4. Database

| Feature | Status | Notes |
|---------|--------|-------|
| SQLite database | [ ] | File-based, no server |
| Users table | [ ] | Store user accounts |
| Tasks table | [ ] | Store tasks |
| User isolation | [ ] | Users can only see their own tasks |
| Data validation | [ ] | Check input before saving |

---

### 5. CLI Interface

| Feature | Status | Notes |
|---------|--------|-------|
| Main menu | [ ] | Login, Register, Exit |
| Task menu | [ ] | Add, List, Complete, Delete, Back |
| Input validation | [ ] | Handle invalid choices |
| Error messages | [ ] | Show helpful error messages |
| Success messages | [ ] | Confirm actions |

---

## MVP User Flow

```
1. User starts app
   ↓
2. Main Menu appears
   ├── Login
   ├── Register
   └── Exit
   ↓
3. User registers/logs in
   ↓
4. Task Menu appears
   ├── Add Task
   ├── List Tasks
   ├── Complete Task
   ├── Delete Task
   ├── View Profile
   └── Logout
   ↓
5. User performs actions
   ↓
6. User logs out
   ↓
7. Back to Main Menu
```

---

## MVP API Endpoints

### Auth Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/register` | Create new user | No |
| POST | `/login` | Get JWT token | No |
| GET | `/me` | Get current user | Yes |

### Task Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/tasks` | Get all user tasks | Yes |
| POST | `/tasks` | Create new task | Yes |
| GET | `/tasks/{id}` | Get task by ID | Yes |
| PUT | `/tasks/{id}` | Update task | Yes |
| DELETE | `/tasks/{id}` | Delete task | Yes |

---

## MVP Success Criteria

### Must Work

- [ ] User can register with username, email, password
- [ ] User can login and get JWT token
- [ ] User can create a task with title, description, priority, deadline
- [ ] User can view all their tasks
- [ ] User can view single task details
- [ ] User can update any task field
- [ ] User can delete a task
- [ ] User can mark task as completed
- [ ] Users cannot see other users' tasks
- [ ] Invalid input shows error messages
- [ ] App doesn't crash on invalid input

### Nice to Have (Not Required for MVP)

- [ ] Search tasks
- [ ] Filter tasks
- [ ] Categories
- [ ] Calendar view
- [ ] Web UI

---

## MVP File Checklist

| File | Purpose | Status |
|------|---------|--------|
| `app/main.py` | FastAPI entry point | [ ] |
| `app/config.py` | Settings | [ ] |
| `app/database.py` | Database connection | [ ] |
| `app/models/user.py` | User table | [ ] |
| `app/models/task.py` | Task table | [ ] |
| `app/schemas/user.py` | User validation | [ ] |
| `app/schemas/task.py` | Task validation | [ ] |
| `app/routes/auth.py` | Auth endpoints | [ ] |
| `app/routes/tasks.py` | Task endpoints | [ ] |
| `app/services/auth.py` | Auth logic | [ ] |
| `app/services/task.py` | Task logic | [ ] |
| `app/utils/security.py` | Password/JWT | [ ] |
| `cli/main.py` | CLI entry point | [ ] |
| `cli/menus.py` | Menu display | [ ] |
| `cli/handlers.py` | Input handling | [ ] |
| `requirements.txt` | Dependencies | [ ] |
| `.env.example` | Environment template | [ ] |
| `.gitignore` | Git ignore rules | [ ] |

---

## How to Use This Checklist

1. Work through `BUILD-ORDER.md` step by step
2. Check off items as you complete them
3. Test each feature before moving on
4. Come back if you get stuck
5. Mark MVP as complete when all "Must Work" items are checked

---

## After MVP is Complete

Once MVP works, move to `FULL-VERSION-CHECKLIST.md` to add:
- Search and filtering
- Categories
- Web UI
- Calendar view
- Settings
- Testing
- Documentation

---

*This checklist tracks MVP completion.*

# Project Structure

## Folder Layout

```
Task-Management-System/
├── app/                          # Main application code
│   ├── __init__.py              # Package init
│   ├── main.py                  # FastAPI app entry point
│   ├── config.py                # Configuration settings
│   ├── database.py              # Database connection
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── user.py              # User model
│   │   └── task.py              # Task model
│   ├── schemas/                 # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py              # User schemas
│   │   └── task.py              # Task schemas
│   ├── routes/                  # API routes
│   │   ├── __init__.py
│   │   ├── auth.py              # Authentication routes
│   │   └── tasks.py             # Task routes
│   ├── services/                # Business logic
│   │   ├── __init__.py
│   │   ├── auth.py              # Authentication logic
│   │   └── task.py              # Task logic
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       └── security.py          # Password hashing, JWT
├── cli/                         # CLI interface
│   ├── __init__.py
│   ├── main.py                  # CLI entry point
│   ├── menus.py                 # Menu displays
│   └── handlers.py              # User input handling
├── tests/                       # Test files
│   ├── __init__.py
│   ├── test_auth.py             # Auth tests
│   └── test_tasks.py            # Task tests
├── static/                      # Static files (for Web UI)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── index.html
├── docs/                        # Documentation
│   ├── API.md                   # API documentation
│   ├── SETUP.md                 # Setup instructions
│   └── USER-GUIDE.md            # User guide
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── README.md                    # Project README
└── TASKS.md                     # Task tracking
```

---

## File Descriptions

### Core Application (`app/`)

| File | Purpose |
|------|---------|
| `main.py` | FastAPI application entry point, starts server |
| `config.py` | Settings, environment variables, configuration |
| `database.py` | SQLite connection, session management |

### Models (`app/models/`)

| File | Purpose |
|------|---------|
| `user.py` | User database table definition |
| `task.py` | Task database table definition |

### Schemas (`app/schemas/`)

| File | Purpose |
|------|---------|
| `user.py` | User data validation (request/response) |
| `task.py` | Task data validation (request/response) |

### Routes (`app/routes/`)

| File | Purpose |
|------|---------|
| `auth.py` | Login, register, logout endpoints |
| `tasks.py` | Task CRUD endpoints |

### Services (`app/services/`)

| File | Purpose |
|------|---------|
| `auth.py` | Authentication business logic |
| `task.py` | Task business logic |

### CLI (`cli/`)

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point, main loop |
| `menus.py` | Display menus to user |
| `handlers.py` | Process user input |

### Tests (`tests/`)

| File | Purpose |
|------|---------|
| `test_auth.py` | Test authentication functions |
| `test_tasks.py` | Test task functions |

### Static Files (`static/`)

| File | Purpose |
|------|---------|
| `index.html` | Main HTML page |
| `style.css` | CSS styles |
| `app.js` | JavaScript for web UI |

---

## Why This Structure?

| Principle | How It's Applied |
|-----------|------------------|
| **Separation of Concerns** | Models, routes, services are separate |
| **Modularity** | Each file has one responsibility |
| **Scalability** | Easy to add new features |
| **Testability** | Tests are separate from app code |
| **Maintainability** | Clear file organization |

---

## Naming Conventions

| Item | Convention | Example |
|------|------------|---------|
| Files | snake_case | `user.py`, `task.py` |
| Classes | PascalCase | `User`, `Task` |
| Functions | snake_case | `create_task`, `get_user` |
| Variables | snake_case | `user_id`, `task_title` |
| Constants | UPPER_SNAKE_CASE | `DATABASE_URL`, `SECRET_KEY` |

---

## Next Steps

1. Read `DATABASE-DESIGN.md` to understand the data model
2. Read `BUILD-ORDER.md` to know what to build first
3. Start with Phase 1: Project Setup

---

*This structure will be created as we build.*

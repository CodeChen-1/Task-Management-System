# Build Order

## Overview

This document shows exactly what to build and in what order. Follow this sequence step by step.

---

## Phase 1: Project Setup

### Step 1.1: Create Project Structure

**What to do:**
1. Create folder structure
2. Create empty `__init__.py` files
3. Create `requirements.txt`
4. Create `.gitignore`
5. Create `.env.example`

**Files to create:**
```
Task-Management-System/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── routes/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── cli/
│   └── __init__.py
├── tests/
│   └── __init__.py
├── static/
├── docs/
├── requirements.txt
├── .gitignore
└── .env.example
```

**Verify by:** Running `ls -la` shows all folders

---

### Step 1.2: Set Up Python Environment

**What to do:**
1. Create virtual environment
2. Activate virtual environment
3. Install basic dependencies

**Commands:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] python-dotenv
pip freeze > requirements.txt
```

**Verify by:** `pip list` shows installed packages

---

### Step 1.3: Initialize Git

**What to do:**
1. Initialize git repository
2. Create first commit

**Commands:**
```bash
git init
git add .
git commit -m "Initial project setup"
```

**Verify by:** `git status` shows clean working directory

---

### Step 1.4: Set Up GitHub Repository

**What to do:**
1. Create GitHub repository
2. Connect local repo to GitHub
3. Push initial code

**Commands:**
```bash
# Create repo on GitHub (via website or GitHub CLI)
# Then connect local repo:
git remote add origin https://github.com/YOUR_USERNAME/Task-Management-System.git
git branch -M main
git push -u origin main
```

**Verify by:** `git remote -v` shows GitHub URL

---

### Step 1.5: Create GitHub Workflow

**What to do:**
1. Create `.github/workflows/` folder
2. Create basic CI workflow (optional, can add later)

**Verify by:** GitHub Actions page shows workflow

---

## Phase 2: Database Implementation

### Step 2.1: Create Database Configuration

**What to do:**
1. Create `app/config.py` for settings
2. Create `app/database.py` for SQLite connection

**Files to create:**
- `app/config.py`
- `app/database.py`

**Verify by:** Running Python script connects to database

---

### Step 2.2: Create User Model

**What to do:**
1. Create `app/models/user.py`
2. Define User table
3. Create database tables

**Files to create:**
- `app/models/user.py`

**Verify by:** Running script creates `users` table in database

---

### Step 2.3: Create Task Model

**What to do:**
1. Create `app/models/task.py`
2. Define Task table
3. Create database tables

**Files to create:**
- `app/models/task.py`

**Verify by:** Running script creates `tasks` table in database

---

## Phase 3: Backend API (MVP)

### Step 3.1: Create User Schemas

**What to do:**
1. Create `app/schemas/user.py`
2. Define Pydantic models for user data

**Files to create:**
- `app/schemas/user.py`

**Verify by:** Importing schemas doesn't cause errors

---

### Step 3.2: Create Task Schemas

**What to do:**
1. Create `app/schemas/task.py`
2. Define Pydantic models for task data

**Files to create:**
- `app/schemas/task.py`

**Verify by:** Importing schemas doesn't cause errors

---

### Step 3.3: Create Security Utilities

**What to do:**
1. Create `app/utils/security.py`
2. Implement password hashing
3. Implement JWT token creation/verification

**Files to create:**
- `app/utils/security.py`

**Verify by:** Can hash password and create/verify JWT token

---

### Step 3.4: Create Auth Service

**What to do:**
1. Create `app/services/auth.py`
2. Implement user registration
3. Implement user login
4. Implement token verification

**Files to create:**
- `app/services/auth.py`

**Verify by:** Can register user and login

---

### Step 3.5: Create Auth Routes

**What to do:**
1. Create `app/routes/auth.py`
2. Create `/register` endpoint
3. Create `/login` endpoint
4. Create `/me` endpoint

**Files to create:**
- `app/routes/auth.py`

**Verify by:** Testing endpoints in Swagger UI

---

### Step 3.6: Create Task Service

**What to do:**
1. Create `app/services/task.py`
2. Implement task CRUD operations
3. Implement user isolation (users can only see their own tasks)

**Files to create:**
- `app/services/task.py`

**Verify by:** Can create, read, update, delete tasks

---

### Step 3.7: Create Task Routes

**What to do:**
1. Create `app/routes/tasks.py`
2. Create `GET /tasks` endpoint
3. Create `POST /tasks` endpoint
4. Create `GET /tasks/{id}` endpoint
5. Create `PUT /tasks/{id}` endpoint
6. Create `DELETE /tasks/{id}` endpoint

**Files to create:**
- `app/routes/tasks.py`

**Verify by:** Testing all endpoints in Swagger UI

---

### Step 3.8: Create Main App

**What to do:**
1. Create `app/main.py`
2. Set up FastAPI app
3. Include routers
4. Add CORS middleware

**Files to create:**
- `app/main.py`

**Verify by:** Running `uvicorn app.main:app` starts server

---

## Phase 4: CLI Interface (MVP)

### Step 4.1: Create CLI Entry Point

**What to do:**
1. Create `cli/main.py`
2. Create main menu loop
3. Handle user choices

**Files to create:**
- `cli/main.py`

**Verify by:** Running `python -m cli.main` shows menu

---

### Step 4.2: Create Menu Display

**What to do:**
1. Create `cli/menus.py`
2. Create main menu
3. Create task menu
4. Create auth menu

**Files to create:**
- `cli/menus.py`

**Verify by:** Menus display correctly

---

### Step 4.3: Create Input Handlers

**What to do:**
1. Create `cli/handlers.py`
2. Handle user input
3. Validate input
4. Call API endpoints

**Files to create:**
- `cli/handlers.py`

**Verify by:** Can interact with app through CLI

---

### Step 4.4: Connect CLI to API

**What to do:**
1. Connect CLI to FastAPI backend
2. Test full flow: register → login → create task → view tasks → logout

**Verify by:** Complete user flow works

---

## Phase 5: MVP Testing

### Step 5.1: Test User Flow

**What to do:**
1. Test registration
2. Test login
3. Test task CRUD
4. Test logout

**Verify by:** All operations work correctly

---

### Step 5.2: Test Error Handling

**What to do:**
1. Test invalid input
2. Test duplicate username
3. Test invalid login
4. Test accessing other user's tasks

**Verify by:** App handles errors gracefully

---

## Phase 6: Enhanced Features

### Step 6.1: Add Search and Filtering

**What to do:**
1. Add search endpoint
2. Add filter by status
3. Add filter by priority

**Verify by:** Can search and filter tasks

---

### Step 6.2: Add Categories

**What to do:**
1. Create Category model
2. Create TaskCategory model
3. Create category CRUD
4. Add category to tasks

**Verify by:** Can create categories and assign tasks

---

## Phase 7: Web UI

### Step 7.1: Create HTML Structure

**What to do:**
1. Create `static/index.html`
2. Create login/register forms
3. Create task list display
4. Create task form

**Verify by:** Opening in browser shows UI

---

### Step 7.2: Add CSS Styles

**What to do:**
1. Create `static/css/style.css`
2. Style forms
3. Style task list
4. Add responsive design

**Verify by:** UI looks good in browser

---

### Step 7.3: Add JavaScript

**What to do:**
1. Create `static/js/app.js`
2. Handle form submissions
3. Make API calls
4. Update UI dynamically

**Verify by:** Can login, create tasks, view tasks in browser

---

## Phase 8: Rich Features

### Step 8.1: Add Calendar View

**What to do:**
1. Create calendar endpoint
2. Group tasks by deadline
3. Display in Web UI

**Verify by:** Can see tasks on calendar

---

### Step 8.2: Add Settings

**What to do:**
1. Create settings page
2. Add dark/light mode toggle
3. Add notification preferences

**Verify by:** Can change settings

---

## Phase 9: Testing & Polish

### Step 9.1: Write Unit Tests

**What to do:**
1. Create `tests/test_auth.py`
2. Create `tests/test_tasks.py`
3. Test all functions

**Verify by:** `pytest` passes all tests

---

### Step 9.2: Write Documentation

**What to do:**
1. Create `README.md`
2. Create `docs/API.md`
3. Create `docs/SETUP.md`
4. Create `docs/USER-GUIDE.md`

**Verify by:** Someone else can set up and use the app

---

## Verification Checkpoints

| Phase | Checkpoint | How to Verify |
|-------|------------|---------------|
| 1 | Project setup complete | All folders exist, git initialized |
| 2 | Database works | Can create/query tables |
| 3 | API works | All endpoints respond correctly |
| 4 | CLI works | Can use app through terminal |
| 5 | MVP complete | Full user flow works |
| 6 | Enhanced features | Search, filter, categories work |
| 7 | Web UI works | Can use app in browser |
| 8 | Rich features | Calendar, settings work |
| 9 | Production ready | Tests pass, docs complete |

---

## How to Use This Document

1. Start with Phase 1
2. Complete each step in order
3. Verify each step before moving to next
4. Check off completed steps
5. Come back if you get stuck

---

*This order will be followed as we build.*

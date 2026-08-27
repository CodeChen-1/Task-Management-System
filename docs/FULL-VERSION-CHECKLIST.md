# Full Version Checklist (Rich Features)

## What is Full Version?

Full version includes all features from the original requirements plus professional touches like testing, documentation, and deployment.

---

## Features to Add After MVP

### 1. Search & Filtering

| Feature | Status | Notes |
|---------|--------|-------|
| Search by title | [ ] | Find tasks by name |
| Search by description | [ ] | Find tasks by content |
| Filter by status | [ ] | pending, in_progress, completed |
| Filter by priority | [ ] | low, medium, high |
| Filter by deadline | [ ] | overdue, upcoming, this week |
| Sort by date | [ ] | newest first, oldest first |
| Sort by priority | [ ] | high to low, low to high |

---

### 2. Categories

| Feature | Status | Notes |
|---------|--------|-------|
| Create category | [ ] | Name + color |
| Edit category | [ ] | Change name/color |
| Delete category | [ ] | Remove category |
| Assign task to category | [ ] | Link task to category |
| Remove task from category | [ ] | Unlink task |
| View tasks by category | [ ] | Filter by category |

---

### 3. Calendar View

| Feature | Status | Notes |
|---------|--------|-------|
| Monthly view | [ ] | Show all tasks in month |
| Daily view | [ ] | Show tasks for specific day |
| Color coding | [ ] | Tasks colored by priority |
| Click to view task | [ ] | Click task to see details |
| Add task from calendar | [ ] | Create task with pre-filled date |

---

### 4. Web UI (HTML/CSS/JS)

| Feature | Status | Notes |
|---------|--------|-------|
| Login page | [ ] | Beautiful login form |
| Register page | [ ] | Registration form |
| Dashboard | [ ] | Overview of tasks |
| Task list | [ ] | Table/card view of tasks |
| Task detail | [ ] | View/edit single task |
| Calendar page | [ ] | Visual calendar |
| Categories page | [ ] | Manage categories |
| Settings page | [ ] | User preferences |
| Responsive design | [ ] | Works on mobile |
| Dark/light mode | [ ] | Theme toggle |

---

### 5. Reminders

| Feature | Status | Notes |
|---------|--------|-------|
| Due soon notification | [ ] | Tasks due in 24 hours |
| Overdue notification | [ ] | Tasks past deadline |
| Desktop notification | [ ] | Browser notification (Web UI) |
| Reminder settings | [ ] | User can configure |

---

### 6. Settings

| Feature | Status | Notes |
|---------|--------|-------|
| Edit profile | [ ] | Change username/email |
| Change password | [ ] | Update password |
| Notification preferences | [ ] | Enable/disable notifications |
| Dark/light mode | [ ] | Theme preference |
| Default sort order | [ ] | How tasks are sorted |
| Default view | [ ] | List or card view |

---

### 7. Testing

| Feature | Status | Notes |
|---------|--------|-------|
| Unit tests - auth | [ ] | Test authentication functions |
| Unit tests - tasks | [ ] | Test task functions |
| Integration tests - API | [ ] | Test API endpoints |
| Test coverage report | [ ] | See what's tested |
| Edge case tests | [ ] | Test error handling |

---

### 8. Documentation

| Feature | Status | Notes |
|---------|--------|-------|
| README.md | [ ] | Project overview |
| Setup instructions | [ ] | How to install and run |
| API documentation | [ ] | Endpoint descriptions |
| User guide | [ ] | How to use the app |
| Developer guide | [ ] | How to contribute |
| Changelog | [ ] | Version history |

---

### 9. Deployment

| Feature | Status | Notes |
|---------|--------|-------|
| Docker setup | [ ] | Containerize app |
| Docker Compose | [ ] | Multi-service setup |
| Environment config | [ ] | Production settings |
| Database migration | [ ] | Schema versioning |
| Health check | [ ] | Monitor app status |

---

## Full Version API Endpoints

### Auth Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/register` | Create new user | No |
| POST | `/login` | Get JWT token | No |
| GET | `/me` | Get current user | Yes |
| PUT | `/me` | Update profile | Yes |
| PUT | `/me/password` | Change password | Yes |

### Task Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/tasks` | Get all user tasks | Yes |
| POST | `/tasks` | Create new task | Yes |
| GET | `/tasks/{id}` | Get task by ID | Yes |
| PUT | `/tasks/{id}` | Update task | Yes |
| DELETE | `/tasks/{id}` | Delete task | Yes |
| GET | `/tasks/search` | Search tasks | Yes |
| GET | `/tasks/filter` | Filter tasks | Yes |

### Category Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/categories` | Get all categories | Yes |
| POST | `/categories` | Create category | Yes |
| PUT | `/categories/{id}` | Update category | Yes |
| DELETE | `/categories/{id}` | Delete category | Yes |
| POST | `/tasks/{id}/categories` | Add task to category | Yes |
| DELETE | `/tasks/{id}/categories/{cat_id}` | Remove from category | Yes |

### Calendar Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/calendar/{year}/{month}` | Get tasks for month | Yes |
| GET | `/calendar/{date}` | Get tasks for day | Yes |

### Settings Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/settings` | Get user settings | Yes |
| PUT | `/settings` | Update settings | Yes |

---

## Full Version Success Criteria

### Must Work

- [ ] All MVP features work
- [ ] Search finds tasks correctly
- [ ] Filtering shows correct results
- [ ] Categories work properly
- [ ] Calendar shows tasks by date
- [ ] Web UI is responsive
- [ ] Dark/light mode works
- [ ] Settings save correctly
- [ ] All tests pass
- [ ] Documentation is complete

### Nice to Have

- [ ] Desktop notifications work
- [ ] Docker deployment works
- [ ] Health check endpoint works
- [ ] Performance is good

---

## How to Use This Checklist

1. Complete MVP first (`MVP-CHECKLIST.md`)
2. Work through features in order
3. Check off items as you complete them
4. Test each feature before moving on
5. Mark full version as complete when all "Must Work" items are checked

---

## Full Version File Checklist

### New Files to Create

| File | Purpose | Status |
|------|---------|--------|
| `app/routes/categories.py` | Category endpoints | [ ] |
| `app/routes/calendar.py` | Calendar endpoints | [ ] |
| `app/routes/settings.py` | Settings endpoints | [ ] |
| `app/services/category.py` | Category logic | [ ] |
| `app/services/calendar.py` | Calendar logic | [ ] |
| `app/services/settings.py` | Settings logic | [ ] |
| `app/models/category.py` | Category table | [ ] |
| `app/models/settings.py` | Settings table | [ ] |
| `app/schemas/category.py` | Category validation | [ ] |
| `app/schemas/settings.py` | Settings validation | [ ] |
| `static/index.html` | Main HTML page | [ ] |
| `static/css/style.css` | CSS styles | [ ] |
| `static/js/app.js` | JavaScript | [ ] |
| `tests/test_auth.py` | Auth tests | [ ] |
| `tests/test_tasks.py` | Task tests | [ ] |
| `tests/test_categories.py` | Category tests | [ ] |
| `docs/API.md` | API documentation | [ ] |
| `docs/SETUP.md` | Setup instructions | [ ] |
| `docs/USER-GUIDE.md` | User guide | [ ] |
| `Dockerfile` | Docker setup | [ ] |
| `docker-compose.yml` | Docker Compose | [ ] |

---

*This checklist tracks full version completion.*

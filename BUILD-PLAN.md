# Build Plan: Task Management System

## Project Overview

| Attribute | Value |
|-----------|-------|
| **Project Name** | Task Management System |
| **Type** | Internal tool for small business |
| **Approach** | MVP first, then rich features |
| **Interface** | CLI (MVP) → Web UI (Full Version) |
| **Backend** | Python + FastAPI |
| **Database** | SQLite |
| **Auth** | JWT tokens |

---

## Build Strategy

### Phase 1: MVP (Minimum Viable Product)
Build the core functionality that works end-to-end.

**What's Included:**
- User authentication (register, login, logout)
- Task CRUD (create, read, update, delete)
- Basic task properties (title, description, status, priority, deadline)
- SQLite database
- CLI interface

**What's NOT Included (Later):**
- Web UI
- Search and filtering
- Categories
- Calendar view
- Reminders
- Settings

---

### Phase 2: Enhanced Features
Add features that make the app more useful.

**What's Included:**
- Search tasks
- Filter by status/priority
- Categories
- Task statistics

---

### Phase 3: Rich Version
Add professional features.

**What's Included:**
- Web UI (HTML/CSS/JS)
- Calendar view
- Reminders
- Settings (dark/light mode, notifications)
- Better error handling
- Testing

---

## Build Order

```
1. Project Setup
   ↓
2. Database Design & Implementation
   ↓
3. Backend API (MVP)
   ↓
4. CLI Interface (MVP)
   ↓
5. Test MVP End-to-End
   ↓
6. Add Search & Filtering
   ↓
7. Add Categories
   ↓
8. Add Web UI
   ↓
9. Add Calendar View
   ↓
10. Add Settings
   ↓
11. Testing & Polish
   ↓
12. Documentation & Deployment
```

---

## Tech Stack

| Layer | Technology | Why This Choice |
|-------|------------|-----------------|
| **Language** | Python 3.10+ | You know it, popular, job market |
| **Backend** | FastAPI | Modern, fast, great docs |
| **Database** | SQLite | No server needed, offline-first |
| **ORM** | SQLAlchemy | Python standard, easy to use |
| **Auth** | JWT (python-jose) | Industry standard |
| **Password Hashing** | bcrypt | Secure, proven |
| **Testing** | pytest | Python standard |
| **CLI** | rich (optional) | Better terminal output |

---

## Key Decisions

### 1. Database Design
- **Users table**: id, username, email, password_hash, created_at
- **Tasks table**: id, user_id, title, description, status, priority, deadline, created_at, updated_at
- **Categories table**: id, user_id, name, color
- **Task_Categories table**: task_id, category_id (many-to-many)

### 2. API Design
- RESTful endpoints
- JSON responses
- JWT authentication
- Proper error codes

### 3. CLI Design
- Menu-based interface
- Clear prompts
- Colored output (optional)
- Input validation

---

## Success Criteria

### MVP Success
- [ ] User can register and login
- [ ] User can create, view, edit, delete tasks
- [ ] Tasks save to database
- [ ] CLI interface works
- [ ] No crashes on invalid input

### Full Version Success
- [ ] All MVP features work
- [ ] Search and filtering work
- [ ] Categories work
- [ ] Web UI is responsive
- [ ] Calendar view shows tasks by date
- [ ] Settings save user preferences
- [ ] All tests pass
- [ ] Documentation is complete

---

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Database design issues | High | Design before coding |
| Authentication bugs | High | Use proven libraries |
| CLI complexity | Medium | Start simple, add features |
| Web UI too complex | Medium | Build after CLI works |
| Testing gaps | Medium | Write tests as you build |

---

## Next Steps

1. Read `PROJECT-STRUCTURE.md` to understand folder layout
2. Read `DATABASE-DESIGN.md` to understand data model
3. Read `BUILD-ORDER.md` to know what to build first
4. Start with Phase 1: Project Setup

---

*This plan will be updated as we build.*

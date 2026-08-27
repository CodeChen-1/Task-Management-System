# Database Design

## Overview

| Property | Value |
|----------|-------|
| **Database** | SQLite |
| **File** | `tasks.db` |
| **ORM** | SQLAlchemy |
| **Location** | Project root directory |

---

## Tables

### 1. Users Table

Stores user account information.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique user ID |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Login username |
| email | VARCHAR(100) | UNIQUE, NOT NULL | User email |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation date |

---

### 2. Tasks Table

Stores task information.

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    priority VARCHAR(10) DEFAULT 'medium',
    deadline TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique task ID |
| user_id | INTEGER | FOREIGN KEY, NOT NULL | Owner of task |
| title | VARCHAR(100) | NOT NULL | Task title |
| description | TEXT | OPTIONAL | Task details |
| status | VARCHAR(20) | DEFAULT 'pending' | pending, in_progress, completed |
| priority | VARCHAR(10) | DEFAULT 'medium' | low, medium, high |
| deadline | TIMESTAMP | OPTIONAL | When task is due |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When task was created |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When task was last modified |

---

### 3. Categories Table

Stores user-defined categories.

```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    color VARCHAR(7) DEFAULT '#007bff',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique category ID |
| user_id | INTEGER | FOREIGN KEY, NOT NULL | Owner of category |
| name | VARCHAR(50) | NOT NULL | Category name |
| color | VARCHAR(7) | DEFAULT '#007bff' | Hex color code |

---

### 4. Task_Categories Table (Many-to-Many)

Links tasks to categories.

```sql
CREATE TABLE task_categories (
    task_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (task_id, category_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);
```

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| task_id | INTEGER | PRIMARY KEY, FOREIGN KEY | Task reference |
| category_id | INTEGER | PRIMARY KEY, FOREIGN KEY | Category reference |

---

## Relationships

```
Users (1) ──────< (Many) Tasks
Users (1) ──────< (Many) Categories
Tasks (Many) >─────< (Many) Categories
```

### Explanation

| Relationship | Type | Description |
|--------------|------|-------------|
| Users → Tasks | One-to-Many | One user has many tasks |
| Users → Categories | One-to-Many | One user has many categories |
| Tasks ↔ Categories | Many-to-Many | Tasks can have multiple categories |

---

## SQL Queries (Common Operations)

### User Operations

```sql
-- Create user
INSERT INTO users (username, email, password_hash) 
VALUES (?, ?, ?);

-- Get user by username
SELECT * FROM users WHERE username = ?;

-- Get user by email
SELECT * FROM users WHERE email = ?;
```

### Task Operations

```sql
-- Create task
INSERT INTO tasks (user_id, title, description, status, priority, deadline) 
VALUES (?, ?, ?, ?, ?, ?);

-- Get all tasks for user
SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC;

-- Get task by ID (with user check)
SELECT * FROM tasks WHERE id = ? AND user_id = ?;

-- Update task
UPDATE tasks 
SET title = ?, description = ?, status = ?, priority = ?, deadline = ?, updated_at = CURRENT_TIMESTAMP 
WHERE id = ? AND user_id = ?;

-- Delete task
DELETE FROM tasks WHERE id = ? AND user_id = ?;

-- Search tasks
SELECT * FROM tasks 
WHERE user_id = ? AND (title LIKE ? OR description LIKE ?);

-- Filter by status
SELECT * FROM tasks WHERE user_id = ? AND status = ?;

-- Filter by priority
SELECT * FROM tasks WHERE user_id = ? AND priority = ?;

-- Get overdue tasks
SELECT * FROM tasks 
WHERE user_id = ? AND deadline < CURRENT_TIMESTAMP AND status != 'completed';

-- Get upcoming tasks
SELECT * FROM tasks 
WHERE user_id = ? AND deadline > CURRENT_TIMESTAMP 
ORDER BY deadline ASC;
```

### Category Operations

```sql
-- Create category
INSERT INTO categories (user_id, name, color) 
VALUES (?, ?, ?);

-- Get all categories for user
SELECT * FROM categories WHERE user_id = ?;

-- Add task to category
INSERT INTO task_categories (task_id, category_id) 
VALUES (?, ?);

-- Get tasks in category
SELECT t.* FROM tasks t
JOIN task_categories tc ON t.id = tc.task_id
WHERE tc.category_id = ? AND t.user_id = ?;

-- Remove task from category
DELETE FROM task_categories 
WHERE task_id = ? AND category_id = ?;

-- Delete category
DELETE FROM categories WHERE id = ? AND user_id = ?;
```

---

## Data Validation Rules

### Users

| Rule | Validation |
|------|------------|
| Username | 3-50 characters, alphanumeric + underscore |
| Email | Valid email format |
| Password | Minimum 8 characters |

### Tasks

| Rule | Validation |
|------|------------|
| Title | 1-100 characters, required |
| Description | Optional, max 1000 characters |
| Status | Must be: pending, in_progress, completed |
| Priority | Must be: low, medium, high |
| Deadline | Must be valid datetime, must be in future (for new tasks) |

### Categories

| Rule | Validation |
|------|------------|
| Name | 1-50 characters, required |
| Color | Valid hex color (#RRGGBB) |

---

## Indexes (For Performance)

```sql
-- Speed up user lookups
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Speed up task queries
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_priority ON tasks(priority);
CREATE INDEX idx_tasks_deadline ON tasks(deadline);

-- Speed up category queries
CREATE INDEX idx_categories_user_id ON categories(user_id);
CREATE INDEX idx_task_categories_task ON task_categories(task_id);
CREATE INDEX idx_task_categories_category ON task_categories(category_id);
```

---

## Migration Strategy

When schema changes:

1. Create new table with new schema
2. Copy data from old table
3. Drop old table
4. Rename new table to old name

For this project, we'll use simple migrations since it's SQLite.

---

## Next Steps

1. Read `BUILD-ORDER.md` to know what to build first
2. Start with Phase 1: Project Setup

---

*This design will be implemented as we build.*

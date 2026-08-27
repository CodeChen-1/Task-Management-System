# Client Request — Task Management System

### Client: Small Business Owner

**Project:** Task Management Application

**Priority:** Medium

**Objective:** Build a simple task management application that our employees can use to organize and track their daily work.

---

## Background

We are a small company with several employees. Currently, we use spreadsheets and chat messages to keep track of work.

This has become difficult because tasks get forgotten, deadlines are missed, and employees don't have a clear overview of what they need to complete.

We would like a small internal application where employees can create and manage their own tasks.

The application should initially run locally, without depending on an internet connection or paid cloud services.

---

## What We Need

### 1. User Accounts

Employees should be able to:

* Create an account
* Log in
* Log out
* View their account information

Each employee should only be able to access their own tasks.

We may add different types of employees in the future, so please design the system in a way that won't make this difficult later.

---

### 2. Task Management

Employees should be able to:

* Create a task
* View their tasks
* Edit a task
* Delete a task
* Mark a task as completed

A task should contain enough information for an employee to understand what needs to be done.

At minimum, we need:

* Task title
* Description
* Priority
* Status
* Deadline
* Creation date
* Last modified date

---

### 3. Task Organization

Employees may have hundreds of tasks over time, so simply displaying every task in one long list won't be very useful.

We would like employees to be able to:

* Search for tasks
* Filter tasks by status
* Filter tasks by priority
* Sort tasks
* View overdue tasks
* View completed tasks
* View upcoming tasks

---

### 4. Deadlines

Deadlines are important to us.

If a task has a deadline, the application should be able to determine whether the task is:

* Upcoming
* Due soon
* Overdue
* Completed

The system should handle dates and times consistently.

We don't want an employee's computer having an incorrect clock to cause problems with task deadlines.

---

### 5. Reminders

Employees should be able to receive reminders for tasks approaching their deadlines.

For example:

> "Task 'Submit monthly report' is due tomorrow."

The exact reminder mechanism is up to you.

Please consider what would work well for an application that initially runs locally.

---

### 6. Calendar

We would like a calendar view where employees can see their tasks based on their deadlines.

For example:

**August 27**

* Finish documentation
* Review pull request

**August 28**

* Submit report

Employees should be able to select a date and see the tasks associated with it.

---

### 7. Categories

Employees should be able to organize tasks into categories.

For example:

* Work
* Personal
* Development
* Meeting
* Urgent

Employees should be able to create their own categories.

---

### 8. Application Settings

The application should have basic settings.

At minimum:

* Change username/profile information
* Change password
* Notification preferences
* Dark/light mode

Please make reasonable decisions about other settings that may be useful.

---

## Technical Requirements

We don't have a dedicated IT department, so we'd like the application to be relatively easy to run and maintain.

### Storage

The application should work **offline**.

Initially, we don't want to pay for cloud hosting or external databases.

The data should therefore be stored locally.

However, we may want cloud synchronization in the future.

---

### Security

User passwords and private tasks must not be stored insecurely.

Users must not be able to access another user's tasks simply by manipulating a request.

Please consider common security problems when designing the application.

---

### Reliability

We don't want users to lose their tasks because of an application crash.

The application should handle invalid input properly rather than crashing.

For example:

* Empty task title
* Invalid deadline
* Invalid login
* Duplicate username
* Attempting to access a task that doesn't belong to the user

---

### Testing

Before we deploy the application, we want confidence that the important functionality works correctly.

Please include automated tests for important parts of the system.

---

### Deployment

We eventually want to give the application to another developer so they can run it on their computer without spending hours configuring the environment.

Please consider how the application could be packaged and deployed.

---

# Important Constraints

We **do not** want you to blindly implement every possible feature.

You should decide:

* What belongs in the first version
* What should be postponed
* How the system should be structured
* What technologies are appropriate
* How the database should be designed
* How the API should work
* What security measures are necessary
* What should be tested

If you think one of our requirements is technically inappropriate, explain the problem and propose a better solution.

---

# Expected Deliverables

At the end of the project, we expect:

1. A working application
2. Source code
3. Database design
4. API documentation
5. Automated tests
6. Setup instructions
7. Basic user documentation
8. Technical documentation explaining your design decisions

---

## One important rule for this exercise

**I am the client.**

Don't ask me:

> "Should I use FastAPI?"

> "Should I use SQLite?"

> "Should I use React?"

> "What database tables should I create?"

Those are **engineering decisions you're expected to make**.

If something is genuinely ambiguous from a business perspective, **ask me as the client**.

For example:

> "Should a task be allowed to have multiple categories, or should each task belong to only one category?"

I can then answer as the client.

---

### Your job now

Treat the description above as if a real client just gave it to you.

**Don't start coding yet.**

Your first job should be to turn this messy client request into proper **requirements → scope → use cases → architecture/design → implementation plan**.

That's much closer to how you'll actually work on a software project—and it's also the kind of thinking that will give you good material to talk about during an internship interview.

# Change Log

All notable changes to this project will be documented in this file.

---

## [2026-08-27 15:30](Malaysia Time) - Initial Project Setup and Build Plan

- **Type:** Added
- **User Request:** User wants to build a Task Management System with AI assistance while learning project building experience
- **Affected Files:** BUILD-PLAN.md, PROJECT-STRUCTURE.md, DATABASE-DESIGN.md, BUILD-ORDER.md, MVP-CHECKLIST.md, FULL-VERSION-CHECKLIST.md, TaskRequirements.md
- **Description:** 
  - Reviewed TaskRequirements.md and created comprehensive build plan
  - Created project structure documentation
  - Designed database schema with 4 tables (users, tasks, categories, task_categories)
  - Defined build order with 9 phases
  - Created MVP checklist with core features (auth, task CRUD, CLI)
  - Created full version checklist with rich features (search, categories, calendar, web UI, settings)
  - Removed learning materials that were initially created by mistake
  - User chose Option C: CLI first (MVP), then Web UI (Full Version)
  - Tech stack: Python + FastAPI + SQLite + JWT authentication

## [2026-08-27 15:45](Malaysia Time) - GitHub Version Control Setup

- **Type:** Added
- **User Request:** User wants to use GitHub for version control
- **Affected Files:** BUILD-ORDER.md, .gitignore, .env.example
- **Description:** 
  - Updated BUILD-ORDER.md to include GitHub repository setup
  - Added Step 1.4 and 1.5 for GitHub configuration
  - Created .gitignore file with Python, IDE, database, and environment variable rules
  - Created .env.example file for environment variable template

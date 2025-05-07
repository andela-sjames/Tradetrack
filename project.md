**Folder-Based CLI Notes Application**. 


---

# 🗂️ Folder Notes CLI – Final Capstone Project

Welcome to your final capstone project on your journey to becoming a world-class Python Software Engineer!

This project challenges you to build a real-world, installable, and testable CLI app that manages notes in folders — combining everything you’ve learned in this course.

---

## 🎯 Project Objective

Build a **command-line notes manager** that:

- Allows users to create, read, update, and delete notes (CRUD).
- Stores notes inside **folders** with labels and limits.
- Uses **in-memory caching** and **SQLite for persistence**.
- Can **import notes from a CSV file**.
- Is installable, testable, and publishable.

---

## 🛠️ Requirements

### 📂 Folders
- Can be **created manually** or generated with **random names**.
- Have **labels** (e.g. "Work", "Ideas").
- Have a **limit of 10 notes**.
- Folder logic must be **abstracted** from the user.

### 📝 Notes
- CRUD support via CLI.
- Assigned to folders automatically.
- Access by **title**.
- Stored in memory before being saved to SQLite.

### 📥 CSV Import
- Import a CSV file with `title`, `content`, and `tag`.
- File path should be accepted via CLI.
- Notes should be **randomly assigned** to folders if not specified.

---

## 📚 Tech Stack

| Area         | Tool |
|--------------|------|
| CLI          | [Typer](https://typer.tiangolo.com) |
| Database     | SQLite + SQLAlchemy / custom ORM |
| Testing      | Pytest + pytest-cov |
| Linting      | flake8 / black |
| Automation   | Makefile |
| Packaging    | `pyproject.toml` + `setuptools` |
| Importing    | `csv` module |
| Version Ctrl | Git & GitHub |

---

## ✅ Functional Checklist

- [ ] CLI supports note CRUD
- [ ] Folders created with labels and limited to 10 notes
- [ ] Notes assigned automatically to folders
- [ ] CSV import functionality implemented
- [ ] In-memory caching before SQLite storage
- [ ] Users access notes by title
- [ ] Code follows clean Python practices
- [ ] Linted with flake8 or black
- [ ] Code coverage ≥ 90%
- [ ] Project is installable (`pip install .`)
- [ ] GitHub repo has clear instructions

---

## 📁 Suggested Folder Structure

```
folder-notes-cli/
├── app/
│   ├── cli.py
│   ├── models.py
│   ├── db.py
│   └── services/
│       ├── folders.py
│       └── notes.py
├── tests/
│   ├── test_notes.py
│   ├── test_folders.py
│   └── test_csv_import.py
├── sample_notes.csv
├── main.py
├── Makefile
├── setup.py or pyproject.toml
├── README.md
```

---

## 🧪 Testing & Automation

- Write unit tests with **Pytest**
- Use **fixtures** for clean test data
- Track test coverage with `pytest-cov`
- Add a `Makefile` for test, lint, and coverage commands

---

## 📈 Bonus Points

Earn extra credit for:
- 🔍 Search functionality (by content/tag)
- 📤 Export notes to HTML or Markdown
- ♻️ Cache eviction logic
- 📊 CLI analytics or reporting features

---

## 📥 CSV File Format Example

```csv
title,content,tag
"Welcome","This is a test note.","personal"
"My Idea","Let's build something cool.","work"
```

---

## 📦 Packaging

Make your project installable and shareable:

```bash
pip install .
```

Test locally, or build for PyPI:

```bash
python -m build
twine upload dist/*
```

---

## 📜 Submission Guidelines

- Push your final project to **GitHub**
- Include a **README** explaining setup, commands, and import process
- Include sample data and installation instructions
- (Optional) Upload to **TestPyPI** or **PyPI**

---

## 🏁 Closing Note

🎉 Completing this project means you:
- Built a full-stack CLI app with persistence and automation.
- Wrote professional-quality Python with tests and packaging.
- Learned how to ship real software.

Now go show the world what you’ve built. Great job!

---

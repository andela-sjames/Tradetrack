

# 📦 TradeTrack CLI

**TradeTrack** is a powerful and user-friendly command-line tool built with Python that helps you manage products, inventory, and transactions (purchases and sales). It's ideal for small business owners, inventory managers, or anyone looking to track stock using the terminal.

---

## 🚀 Features

- 📦 Add and manage product information (name, SKU, category, price)
- 💰 Record purchases and sales with quantity and price
- 📊 Generate profit reports
- 📈 View current inventory status
- 📁 Data stored in SQLite with SQLAlchemy ORM
- 🧪 Unit-tested with Pytest and coverage reporting
- ⚙️ Easily installable as a CLI tool using `pip`

---

## 🛠️ Installation

```bash
# Clone the repository
git clone git@github.com:andela-sjames/Tradetrack.git
cd Tradetrack

# Install the app (editable/development mode)
pip install .
```

---

## 💻 Usage

After installing, the CLI tool can be accessed with:

```bash
tradetrack
```

### Example Commands

```bash
tradetrack --help
tradetrack add-product
tradetrack record-purchase
tradetrack record-sale
tradetrack inventory-status
tradetrack profit-report
```

Typer will guide you interactively through prompts for required fields.

---

## 📂 Project Structure

```
tradetrack/
├── app/
│   ├── cli.py          # CLI commands (Typer app)
│   ├── db.py           # DB setup and session
│   ├── models.py       # SQLAlchemy models
├── tests/
│   ├── test_inventory.py
│   ├── test_transactions.py
│   └── test_reports.py
├── main.py             # CLI entry point
├── setup.py / pyproject.toml
├── Makefile
├── README.md
```

---

## ✅ Makefile Commands

| Command         | What It Does                           |
|-----------------|----------------------------------------|
| `make test`     | Run all tests using Pytest             |
| `make coverage` | Show test coverage in terminal         |
| `make htmlcov`  | Generate and open HTML coverage report |

 
---

### TODO! 


| Command         | What It Does                           |
|-----------------|----------------------------------------|
| `make lint`     | Run `flake8` to check code style       |
| `make clean`    | Remove temp files and caches           |


---

## 🧪 Testing

This project uses **Pytest** for unit tests.

```bash
make test       # Run tests
make coverage   # View test coverage
```

Target: **90%+ coverage**

---

## 📦 Packaging

To build and install the app as a Python package:

```bash
python -m build
pip install dist/tradetrack-*.whl
```

To publish:

```bash
twine upload dist/*
```

---

## 📄 Requirements

- Python 3.8+
- Typer
- SQLAlchemy
- Pytest, pytest-cov
- setuptools, build, twine

Install them with:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

📧 [svjamesblog@gmail.com.com]  
🐙 [GitHub Profile](https://github.com/andela-sjames)

---

## 📜 License

This project is licensed under the **MIT License** — use it freely, just give credit!

---

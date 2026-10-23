# FinTrack CLI 💰

A simple **command-line expense tracker** written in Python.

> 🇧🇷 Controle de gastos pessoais pelo terminal, feito em Python.

## ✨ Features

- Add an expense (name + amount)
- List all expenses
- Show the total spent
- Input validation: negative amounts are rejected
- Unit tests with **pytest** and CI with **GitHub Actions**

## 🚀 Running locally

```bash
git clone https://github.com/thalesdias99/fintrack-cli.git
cd fintrack-cli
pip install -r requirements.txt
python -m src.app
```

```
1 - Adicionar gasto
2 - Listar gastos
3 - Total
4 - Sair
```

## 🧪 Running the tests

```bash
pytest
```

## 📁 Project structure

```
fintrack-cli/
├── src/app.py          # application logic and menu
├── tests/test_app.py   # unit tests
└── .github/workflows/  # CI pipeline
```

## 🔜 Next steps

- Save expenses to a file (JSON/CSV) so data persists between runs
- Add categories and monthly reports

---

Made by [Thales Freitas](https://www.linkedin.com/in/thales-freitas-64527924a)

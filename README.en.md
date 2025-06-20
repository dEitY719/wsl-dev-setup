# wsl-dev-setup

[kr-한국어](README.md) | **[en-English]**

This is an automation script to help you quickly set up a Python development environment in WSL (Windows Subsystem for Linux).
It is configured to install and manage multiple Python versions through `pyenv`.

## ✅ Purpose

- Automate initial setup of WSL development environment
- Manage Python versions through `pyenv`
- Automatically install multiple Python versions from 3.9 to 3.13
- Automatically add pyenv settings to `.bashrc` or `.zshrc`

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/dEitY719/wsl-dev-setup.git
cd wsl-dev-setup
```

### 2. Install system packages (install dependencies)

```bash
python3 setup_pyenv.py
```

> On some systems, you may need to use `python3` instead of `python`.

## 📂 Structure

- `setup_pyenv.py`: Automation script for full pyenv installation and Python version configuration
- `README.md`: Documentation
- `README.en.md`: Documentation (English)

## 🛠 List of Python versions to be installed

- 3.9.22
- 3.10.17
- 3.11.12
- 3.12.10
- 3.13.3

This list can be modified in `PYTHON_LIST` within `setup_pyenv.py`.

## Code Quality Automation with tox

This project uses `tox` to automate code formatting, linting, and type checking.

### Purpose

- Ensure consistent code style
- Automate static analysis and early error detection
- Easily run all or individual checks

### How to Use

- Run all checks:

```bash
  tox
```

- Run individual checks:

```bash
tox -e black    # Run code formatter and apply fixes
tox -e isort    # Sort imports
tox -e mypy     # Perform type checking
tox -e pylint   # Run linter
tox -e lint     # Shortcut to run only pylint
```

- You can configure the target directory or files by setting the `targetdir` environment variable in `tox.ini`. The default is the current directory (`.`).

### Notes

- Required tools will be installed automatically in the tox virtual environment.
- Python 3.7+ is required.

## 🔄 Additional Notes

- The existing Python3 system package will be removed and managed based on pyenv.
- Pyenv related settings are automatically added to `.bashrc` or `.zshrc`.
- After running the script, run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

## 📝 License

[MIT License](LICENSE) 
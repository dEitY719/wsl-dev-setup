# wsl-dev-setup

WSL(Windows Subsystem for Linux) 환경에서 Python 개발 환경을 빠르게 설정할 수 있도록 돕는 자동화 스크립트입니다.  
`pyenv`를 통해 여러 Python 버전을 설치하고 관리할 수 있도록 구성됩니다.


## ✅ 목적

- WSL 개발 환경 초기 세팅 자동화
- `pyenv`를 통한 Python 버전 관리
- Python 3.9 ~ 3.13까지 여러 버전을 자동 설치
- `.bashrc` 또는 `.zshrc`에 pyenv 설정 자동 추가


## 🚀 사용방법

### 1. 저장소 클론

```bash
git clone https://github.com/dEitY719/wsl-dev-setup.git
cd wsl-dev-setup
````

### 2. 시스템 패키지 설치 (의존성 설치)

```bash
python3 setup_pyenv.py
```

> 일부 시스템에서는 `python` 대신 `python3`를 사용해야 할 수 있습니다.


## 📂 구성

* `setup_pyenv.py`: 전체 pyenv 설치 및 Python 버전 설정 자동화 스크립트
* `README.md`: 설명 문서


## 🛠 설치되는 Python 버전 목록

* 3.9.22
* 3.10.17
* 3.11.12
* 3.12.10
* 3.13.3

이 목록은 `setup_pyenv.py` 내 `PYTHON_LIST`에서 수정할 수 있습니다.


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
````

* Run individual checks:

```bash
tox -e black    # Run code formatter and apply fixes
tox -e isort    # Sort imports
tox -e mypy     # Perform type checking
tox -e pylint   # Run linter
tox -e lint     # Shortcut to run only pylint
```

* You can configure the target directory or files by setting the `targetdir` environment variable in `tox.ini`. The default is the current directory (`.`).


### Notes

* Required tools will be installed automatically in the tox virtual environment.
* Python 3.7+ is required.



## 🔄 참고 사항

* 기존 Python3 시스템 패키지는 제거되며, pyenv 기반으로 관리됩니다.
* `.bashrc` 또는 `.zshrc`에 pyenv 관련 설정이 자동 추가됩니다.
* 적용을 위해 스크립트 실행 후 `source ~/.bashrc` 또는 `source ~/.zshrc`를 실행하세요.


## 📝 License
MIT License

# wsl-dev-setup

**[kr-한국어]** | [en-English](README.en.md)

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
```

### 2. 시스템 패키지 설치 (의존성 설치)

```bash
python3 setup_pyenv.py
```

> 일부 시스템에서는 `python` 대신 `python3`를 사용해야 할 수 있습니다.

## 📂 구성

- `setup_pyenv.py`: 전체 pyenv 설치 및 Python 버전 설정 자동화 스크립트
- `README.md`: 설명 문서
- `README.en.md`: 설명 문서 (영문)

## 🛠 설치되는 Python 버전 목록

- 3.9.22
- 3.10.17
- 3.11.12
- 3.12.10
- 3.13.3

이 목록은 `setup_pyenv.py` 내 `PYTHON_LIST`에서 수정할 수 있습니다.

## tox를 이용한 코드 품질 자동화

이 프로젝트는 `tox`를 사용하여 코드 포맷팅, 린팅, 타입 체킹을 자동화합니다.

### 목적

- 일관된 코드 스타일 유지
- 정적 분석 및 조기 오류 감지 자동화
- 전체 또는 개별 검사를 쉽게 실행

### 사용 방법

- 모든 검사 실행:

```bash
  tox
```

- 개별 검사 실행:

```bash
tox -e black    # 코드 포맷터 실행 및 수정 사항 적용
tox -e isort    # import 정렬
tox -e mypy     # 타입 체킹 수행
tox -e pylint   # 린터 실행
tox -e lint     # pylint만 실행하는 단축 명령어
```

- `tox.ini`에서 `targetdir` 환경 변수를 설정하여 대상 디렉터리 또는 파일을 구성할 수 있습니다. 기본값은 현재 디렉터리 (`.`)입니다.

### 참고

- 필요한 도구는 tox 가상 환경에 자동으로 설치됩니다.
- Python 3.7 이상이 필요합니다.

## 🔄 참고 사항

- 기존 Python3 시스템 패키지는 제거되며, pyenv 기반으로 관리됩니다.
- `.bashrc` 또는 `.zshrc`에 pyenv 관련 설정이 자동 추가됩니다.
- 적용을 위해 스크립트 실행 후 `source ~/.bashrc` 또는 `source ~/.zshrc`를 실행하세요.

## 📝 라이선스

[MIT 라이선스](LICENSE)

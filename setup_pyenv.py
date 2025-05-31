import os
import shutil
import subprocess
from pathlib import Path

PYTHON_LIST = ["3.9.22", "3.10.17", "3.11.12", "3.12.10", "3.13.3"]
SHELL_RC = Path.home() / ".bashrc"  # 또는 ".zshrc" 등 사용자 쉘에 맞게 수정


def run(cmd: str) -> None:
    print(f"🔧 실행 중: {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def remove_non_system_pythons() -> None:
    print("🚫 Ubuntu 기본 Python3은 유지하고, 기타 Python 패키지를 제거합니다...")

    # 기본 python3 패키지를 확인하여 보존할 버전 결정
    result = subprocess.run(
        "python3 -V", shell=True, capture_output=True, text=True, check=True
    )
    system_python_version = (
        result.stdout.strip().split()[1] if result.returncode == 0 else None
    )
    print(f"🔍 시스템 Python3 버전: {system_python_version}")

    # system python3은 제외한 나머지 python3.X 패키지 삭제
    run(
        r"sudo apt remove -y $(dpkg --get-selections | grep -E '^python3\.[0-9]+' | "
        r"cut -f1 | grep -v python3.10 || true)"
    )
    run("sudo apt remove -y libpython3-dev libpython3-all-dev || true")
    run("sudo apt autoremove -y")
    run(
        r"sudo apt purge -y $(dpkg --get-selections | grep -E '^python3\.[0-9]+' | "
        r"cut -f1 | grep -v python3.10 || true)"
    )
    print("✅ 비시스템 Python 패키지 제거 완료.")


def remove_existing_pythons() -> None:
    print("🚫 Python3 전체를 삭제하려다 오류가 발생했으므로, 안전하게 진행합니다...")

    # python3 자체는 남기되, 개별 버전 및 라이브러리만 제거
    removable = """
sudo apt remove -y python3.9 python3.9-* \
    python3.10 python3.10-* \
    python3.11 python3.11-* \
    python3.12 python3.12-* \
    python3.13 python3.13-* \
    libpython3.9 libpython3.10 libpython3.11 \
    libpython3.12 libpython3.13 \
    libpython3.9-dev libpython3.10-dev \
    libpython3.11-dev libpython3.12-dev libpython3.13-dev || true
"""
    run(removable)
    run("sudo apt autoremove -y || true")
    run("sudo apt purge -y $(dpkg -l | grep '^rc' | awk '{print $2}') || true")
    print("✅ 대부분의 기존 Python 패키지 제거 완료 (시스템 Python은 유지).")


def install_dependencies() -> None:
    print("📦 필수 패키지 설치 중...")
    run("sudo apt update")
    run(
        """sudo apt install -y make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncurses-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
        libffi-dev liblzma-dev git"""
    )


def install_pyenv() -> None:
    if shutil.which("pyenv"):
        print("✅ pyenv가 이미 설치되어 있습니다.")
        return

    print("📥 pyenv 설치 중...")
    run("curl https://pyenv.run | bash")

    # 쉘 설정에 pyenv 환경 변수 추가
    pyenv_init = """
# >>> pyenv >>>
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
# <<< pyenv <<<
"""
    with open(SHELL_RC, "a", encoding="utf-8") as f:
        f.write(pyenv_init)

    print(f"✅ {SHELL_RC}에 pyenv 초기화 코드가 추가되었습니다.")
    print("🔁 터미널을 재시작하거나, source ~/.bashrc를 실행하세요.")


def install_python_versions() -> None:
    os.environ["PYENV_ROOT"] = str(Path.home() / ".pyenv")
    os.environ["PATH"] = f"{os.environ['PYENV_ROOT']}/bin:" + os.environ["PATH"]

    for version in PYTHON_LIST:
        print(f"⬇️ Python {version} 설치 중...")
        run(f"pyenv install -s {version}")

    print("🎯 설치된 Python 버전 목록:")
    run("pyenv versions")


def append_pyenv_to_shell_rc() -> None:
    # 현재 쉘 감지하여 알맞은 rc 파일 선택
    shell = os.environ.get("SHELL", "")
    if "zsh" in shell:
        shell_rc = Path.home() / ".zshrc"
    else:
        shell_rc = Path.home() / ".bashrc"

    pyenv_init = """
# >>> pyenv >>>
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH="$PYENV_ROOT/shims:$PATH"
# <<< pyenv <<<
"""

    with open(shell_rc, "a", encoding="utf-8") as f:
        f.write(pyenv_init)

    print(f"✅ {shell_rc}에 pyenv 초기화 코드가 추가되었습니다.")


def main() -> None:
    install_dependencies()
    install_pyenv()
    install_python_versions()
    append_pyenv_to_shell_rc()

    # remove_existing_pythons()
    # remove_non_system_pythons()
    print("✅ 모든 작업이 완료되었습니다!")


if __name__ == "__main__":
    main()

import subprocess


def run_simple_analysis_with_pytype(project_path: str) -> str:
    """
    Запускает лёгкий анализ кода с использованием pytype.

    Параметры:
    - **project_path**: Путь к проекту, который нужно проанализировать.

    Возвращает:
    - Результат анализа в виде строки.
    """
    result = subprocess.run(["pytype", project_path], capture_output=True, text=True)
    return result.stdout


def run_ai_analysis_with_bandit(project_path: str) -> str:
    """
    Запускает сложный анализ кода с использованием bandit.

    Параметры:
    - **project_path**: Путь к проекту, который нужно проанализировать.

    Возвращает:
    - Результат анализа в виде строки.
    """
    result = subprocess.run(
        ["bandit", "-r", project_path], capture_output=True, text=True
    )
    return result.stdout

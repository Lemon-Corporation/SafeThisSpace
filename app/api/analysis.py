from fastapi import APIRouter, Header
from typing import Optional
from services.analysis_service import (
    run_simple_analysis_with_pytype,
    run_ai_analysis_with_bandit,
)

router = APIRouter()


@router.post("/{id}/analyze/simple", summary="Запуск лёгкого анализа проекта")
async def simple_analysis(id: str, authorization: Optional[str] = Header(None)):
    """
    Запускает лёгкий анализ кода проекта с использованием pytype.

    Параметры:
    - **id**: Идентификатор проекта.
    - **Authorization**: JWT-токен в заголовке запроса.

    Возвращает:
    - **message**: Сообщение о завершении анализа.
    - **result**: Результат анализа.
    """
    project_path = f"projects/{id}"
    result = run_simple_analysis_with_pytype(project_path)
    return {"message": "Simple analysis completed", "result": result}


@router.post("/{id}/analyze/ai", summary="Запуск AI-анализа проекта")
async def ai_analysis(id: str, authorization: Optional[str] = Header(None)):
    """
    Запускает сложный анализ кода проекта с использованием bandit.

    Параметры:
    - **id**: Идентификатор проекта.
    - **Authorization**: JWT-токен в заголовке запроса.

    Возвращает:
    - **message**: Сообщение о завершении анализа.
    - **result**: Результат анализа.
    """
    project_path = f"projects/{id}"
    result = run_ai_analysis_with_bandit(project_path)
    return {"message": "AI analysis completed", "result": result}


@router.get("/{id}/analyze/status", summary="Получение статуса анализа")
async def analysis_status(id: str, authorization: Optional[str] = Header(None)):
    """
    Возвращает статус выполнения анализа проекта.

    Параметры:
    - **id**: Идентификатор проекта.
    - **Authorization**: JWT-токен в заголовке запроса.

    Возвращает:
    - **status**: Текущий статус выполнения задачи.
    """
    return {"status": "In Progress"}

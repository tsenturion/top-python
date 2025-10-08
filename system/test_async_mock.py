"""
Вы создаёте сервис, который получает данные с внешнего API. Для упрощения API представим в виде асинхронной функции fetch_data.
Создайте функцию process_data, которая:
вызывает fetch_data()
возвращает список только тех элементов, которые больше 10

Напишите тест для функции process_data с помощью pytest-asyncio:
Используйте AsyncMock и patch, чтобы замокать fetch_data.
Проверьте, что process_data корректно обрабатывает возвращаемые данные.
Проверьте, что мок вызывается ровно один раз.

Смоделируйте ситуацию, когда fetch_data выбрасывает исключение TimeoutError и убедитесь, что process_data корректно реагирует.
"""
import pytest
from unittest.mock import AsyncMock, patch

from app import process_data
    
@pytest.mark.asyncio
async def test_process_data_normal():
    with patch('app.fetch_data', new_callable=AsyncMock) as mocked_fetch:
        mocked_fetch.return_value = [1, 12, 7, 20]
        result = await process_data()

        assert result == [12, 20]
        mocked_fetch.assert_awaited_once()

@pytest.mark.asyncio
async def test_process_data_timeout():
    with patch('app.fetch_data', new_callable=AsyncMock) as mocked_fetch:
        mocked_fetch.side_effect = TimeoutError("Timeout")
        result = await process_data()

        assert result == []
        mocked_fetch.assert_awaited_once()
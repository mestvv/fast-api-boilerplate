# Fast API Boilerplate

## Установка зависимостей

Проект использует `uv` для управления зависимостями и требует Python 3.13.

### Предварительные требования

1. Установите Python 3.13 (версия указана в `.python-version`)
2. Установите `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Установка зависимостей проекта

```bash
uv sync
```

Эта команда создаст виртуальное окружение и установит все зависимости, указанные в `pyproject.toml`.

## Запуск

### 1. Запуск зависимостей (MySQL)

Запустите MySQL через Docker Compose:

```bash
make compose
```

Или напрямую:

```bash
docker-compose -f docker-compose.yaml up -d
```

MySQL будет доступен на порту `3311` с учетными данными:
- Пользователь: `root`
- Пароль: `root`
- База данных: `root`

### 2. Запуск приложения

Запустите FastAPI приложение:

```bash
uv run uvicorn src.app.main:app --reload
```

Приложение будет доступно по адресу: http://localhost:8000

Документация API доступна по адресу: http://localhost:8000/docs

### Остановка зависимостей

Для остановки MySQL контейнера:

```bash
make compose-down
```

Или напрямую:

```bash
docker-compose -f docker-compose.yaml down
```
## Приложение для учета личных расходов по банковским выпискам


![Version](https://img.shields.io/badge/version-0.1.0--alpha-blue)
![Status](https://img.shields.io/badge/status-in__development-orange)

> ⚠️ **Важно:** Проект находится на стадии разработки.

### Стек
* **Язык**: Python
* **Интерфейс**: Streamlit (в дальнейшем переход на FastApi + React)
* **Анализ данных**: Pandas
* **Визуализация**: Plotly
* **База данных**: SQLite + SQLAlchemy 2.0 (ORM) (в дальнейшем переход на Postgres)
* **Безопасность**: Bcrypt (хэширование паролей)

### 🗺️ Дорожная карта (Roadmap)
- [x] Базовый интерфейс
- [x] Инициализация базы данных SQLite и моделей SQLAlchemy
- [ ] Доработка интерфейса
- [ ] Авторизация
- [ ] Разработка логики парсеров под конкретные банковские выписки
- [ ] Создание интерфейса дашбордов и интерактивных графиков
- [ ] Переход на стек FastAPI + React
- [ ] Миграция с SQLite на PostgreSQL


### Запуск на Linux / macOS:
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `streamlit run main.py`

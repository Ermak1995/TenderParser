# Tender Parser

Мини-приложение на Python для парсинга тендеров с сайта [rostender.info](https://rostender.info/extsearch), сохранения их в CSV и предоставления данных через FastAPI.

---

## Стек
- **Python** — основной язык
- **BeautifulSoup4** — парсинг HTML
- **FastAPI** — веб-интерфейс (REST API)
- **requests** — HTTP-запросы
- **csv** — сохранение данных в файл
- **argparse** — CLI-интерфейс

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Ermak1995/TenderParser.git
   cd TenderParser
2. Установите зависимости
   ```bash
   pip install -r requirements.txt

## Использование
- ### CLI
   ```bash
   python main.py --max 10 --output tenders.csv
   ```
   `--max`	Количество тендеров для парсинга
   
   `--output`	Путь к CSV-файлу

- ### API-интерфейс
   Запуск FastAPI-сервера:
   ```bash
   python -m uvicorn api:app --reload
   ```
   
   Получение информации о тендерах (`GET /tenders`)
   ```bash
   curl -X GET "http://localhost:8000/tenders"
   ```

## Возможные улучшения

- Кеширование и сохранение в базу данных

- Фильтрация по параметрам (регион, заказчик и т.д.)

- Docker-сборка для удобства развёртывания
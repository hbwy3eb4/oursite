$readme = @"
# Учебный проект: Единая платформа организации

## Описание
Внутренняя система для моделирования работы организации с 8 отделами.
Каждый участник — руководитель своего отдела, отвечает за бизнес-процессы модуля.

## Структура проекта

\`\`\`
oursite/  
├── core/                      # ОБЩЕЕ приложение (модели для всех)     
│   ├── models.py              → Employee, Department, Position  
│   └── ...   
├── home/                      # Главная страница + базовый шаблон   
│   ├── templates/   
│   │   ├── base.html          ← Шапка сайта с навигацией   
│   │   └── home/index.html   
│   └── ...  
├── app_ArtemR/                # [Название отдела]  
├── app_Blue_Side/             # [Название отдела]  
├── app_dd/                    # [Название отдела]  
├── app_German/                # [Название отдела]  
├── app_Islam/                 # [Название отдела]  
├── app_Kir_Tarasov/           # [Название отдела]  
├── app_Vica/                  # [Название отдела]  
├── app_Vyacheslav/            # [Название отдела]  
├── oursite/                   # Конфигурация проекта  
│   ├── settings.py  
│   ├── urls.py                # Роутинг на все приложения  
│   └── ...  
├── manage.py  
├── requirements.txt  
└── db.sqlite3                 # Единая база данных (создаётся автоматически)  
\`\`\`

## Быстрый старт

### 1. Установка зависимостей
\`\`\`bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### 2. Применение миграций
\`\`\`bash
python manage.py migrate
\`\`\`

### 3. Запуск сервера
\`\`\`bash
python manage.py runserver
\`\`\`

Открой: http://127.0.0.1:8000/

## Правила работы

### Общие модели
Все общие сущности (Сотрудник, Отдел, Должность) находятся в **core/models.py**.
Импортировать так:
\`\`\`python
from core.models import Employee, Department
\`\`\`

**НЕ создавай** свои модели Employee/Department в своём приложении — будет конфликт.

### Твоё приложение
1. Модели пиши в `app_*/models.py`
2. Views в `app_*/views.py`
3. URL в `app_*/urls.py`
4. Шаблоны в `app_*/templates/app_*/`

### Миграции
После изменения models.py:
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

**Важно:** не коммить чужие миграции из папок других приложений.

### Git
- Работай в своей ветке: `feature/твой_отдел`
- Не пушь напрямую в main/master
- Создавай Pull Request для интеграции

## Отделы и ответственность

| Участник    | Отдел         | Модуль          |
|-------------|---------------|-----------------|
| ArtemR      | Хозяйственный | app_ArtemR      |
| Blue_Side   | [Отдел]       | app_Blue_Side   |
| dd          | [Отдел]       | app_dd          |
| German      | [Отдел]       | app_German      |
| Islam       | [Отдел]       | app_Islam       |
| Kir_Tarasov | [Отдел]       | app_Kir_Tarasov |
| Vica        | [Отдел]       | app_Vica        |
| Vyacheslav  | Воинский учёт | app_Vyacheslav  |

## Бизнес-процессы (ТЗ от преподавателя)

1. **Древо подчинения** — иерархия отделов и сотрудников
2. **Канбан-доска** — 4 столбца: Новая → В работе → На проверке → Выполнено/Просрочено
3. **Уведомления** — автоматические алерты (медосмотр, инструктаж)
4. **Маршрутизация заявок** — фото/заявка от одного отдела к другому
5. **Трекер закупок** — статус контрактов

## Контакты
- Преподаватель: 2 консультации по предметной области
- Никита (сисадмин): 3 консультации по коду
- Общий чат Telegram

## Технологии
- Python 3.15
- Django 6.1.3
- SQLite (для разработки)
- VS Code

###Шаг 3. Инструкция для нового ПК 
# 1. Клонировать репозиторий
git clone (https://github.com/hbwy3eb4/oursite.git)
cd oursite

# 2. Создать виртуальное окружение
python -m venv venv

# 3. Активировать (Windows)
venv\Scripts\activate

# 4. Установить зависимости
pip install -r requirements.txt

# 5. Применить миграции (создаст db.sqlite3)
python manage.py migrate

# 6. Запустить сервер
python manage.py runserver
---
*Последнее обновление: 24.11.2026*
"@

Set-Content -Path "README.md" -Value $readme -Encoding UTF8

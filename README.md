# Bank Guard Panel

Утилита для охранника банка: подключается к удалённой БД и выводит информацию о пропусках сотрудников. Работает через Django ORM, без запуска веб-сервера.

---

## Environment(Окружение)

Python 3.10+ 
PostgreSQL (удалённый, настройки ниже)  
Работа в виртуальном окружении (`venv`)

---

## Requirements(Зависимости)

Установите зависимости из `requirements.txt`:

```
pip install -r requirements.txt
```

Содержимое:

```
Django==3.2.12  
psycopg2==2.9.3
```

---

## Environment variables(Переменные окружения)

Используются настройки подключения к базе данных. Они прописаны напрямую в `settings.py`.

### How to get(Как получить)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'checkpoint.devman.org',
        'PORT': 5434,
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}
```

---

## Run(Запуск)

1. Активируйте виртуальное окружение:

    ```
    venv\Scripts\activate
    ```

2. Запустите скрипт:

    ```
    python main.py
    ```

Вы увидите список пропусков и их статус.

---

## Notes(Примечания)

- Скрипт работает без запуска сервера Django.
- Используется только ORM, `main.py` — точка входа.
- База данных подключена в режиме read-only.

---
# Тестовое задание

Для запуска, нужно установить:

- `>=python3.10`
- `poetry`

Создать `.env` файл со следующим содержимым:

```
DJANGO_SECRET_KEY="xa^0^7q=n7e_4gljb^rx(p%zwv7s%1cblmzm42u&t*183-()^$"
```

И выполнить следующие команды в корневой директории проекта:

```
poetry shell
export $(cat .env | xargs)
python manage.py runserver
```

После чего перейти на http://127.0.0.1:8000/

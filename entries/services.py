import csv
from uuid import uuid4

from django.conf import settings


CSV_DB_PATH = settings.BASE_DIR / 'db.csv'

CSV_FIELDNAMES = ['id', 'Название', 'Вес', 'Цвет']


def _prepare_entry(entry_data: dict) -> dict:
    """
    Подготавливает данные к сохранению в CSV файл: меняет названия
    полей на русские
    """
    entry = {}
    entry_id = uuid4()
    entry['id'] = entry_id
    entry['Название'] = entry_data['title']
    entry['Вес'] = entry_data['weight']
    entry['Цвет'] = entry_data['color']
    return entry


def create_entry_in_csv(entry_data: dict) -> str:
    """
    Создает запись в CSV файле на основе полученных от пользователя
    валидированных данных
    """
    entry = _prepare_entry(entry_data)
    open_mode = 'a' if CSV_DB_PATH.exists() else 'w'
    with open(CSV_DB_PATH, open_mode, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        if open_mode == 'w': writer.writeheader()
        writer.writerow(entry)

    return str(entry['id'])


def _restruct_entry(entry_data) -> dict:
    """
    Изменяет названия полей на английские в полученной из CSV файла записи
    для удобства взаимодействия с этой записью в других частях программы
    """
    entry = {}
    entry['id'] = entry_data['id']
    entry['title'] = entry_data['Название']
    entry['weight'] = entry_data['Вес']
    entry['color'] = entry_data['Цвет']
    return entry


def get_all_csv_entries() -> list[dict | None]:
    """Возвращает все записи из csv файла"""
    if not CSV_DB_PATH.exists: return []
    with open(CSV_DB_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [_restruct_entry(row) for row in reader]

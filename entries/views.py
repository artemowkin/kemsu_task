from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from django.forms.utils import ErrorDict

from .services import create_entry_in_csv, get_all_csv_entries
from .forms import EntryForm


class CreateEntryView(View):
    ERROR_MESSAGES = {
        'title': 'Название должно содержать текст от 3 до 120 символов включительно',
        'weight': 'Вес должен быть целым числом от 1 до 500 включительно',
    }

    def get(self, request: HttpRequest):
        """Страница с формой добавления записи в CSV файл"""
        return render(request, 'create.html')

    def _get_errors(self, errors: ErrorDict):
        """
        Возвращает список сообщений об ошибках на русском языке
        для каждого поля
        """
        return [self.ERROR_MESSAGES[field] for field in errors]

    def post(self, request: HttpRequest):
        """Обработка данных, полученных от формы в POST запросе"""
        form = EntryForm(request.POST)
        if form.is_valid():
            created_entry_id = create_entry_in_csv(form.cleaned_data)
            message = f"Добавлена запись ID={created_entry_id}"
            return render(request, 'create.html', {'message': message})

        errors = self._get_errors(form.errors)
        return render(request, 'create.html', {'form': form, 'errors': errors})


def all_entries(request):
    """Страница со всеми записями в CSV файле"""
    entries = get_all_csv_entries()
    return render(request, 'list.html', {'entries': entries})

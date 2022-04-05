from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

from .services import create_entry_in_csv, get_all_csv_entries
from .forms import EntryForm


class CreateEntryView(View):

    def get(self, request: HttpRequest):
        """Страница с формой добавления записи в CSV файл"""
        form = EntryForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request: HttpRequest):
        """Обработка данных, полученных от формы в POST запросе"""
        form = EntryForm(request.POST)
        if form.is_valid():
            created_entry_id = create_entry_in_csv(form.cleaned_data)
            empty_form = EntryForm()
            message = f"Добавлена запись ID={created_entry_id}"
            return render(request, 'create.html', {
                'form': empty_form, 'message': message
            })

        return render(request, 'create.html', {'form': form})


def all_entries(request):
    """Страница со всеми записями в CSV файле"""
    entries = get_all_csv_entries()
    return render(request, 'list.html', {'entries': entries})

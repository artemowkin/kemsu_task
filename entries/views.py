from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

from .services import create_entry_in_csv, get_all_csv_entries
from .forms import EntryForm


class CreateEntryView(View):

    def get(self, request: HttpRequest):
        form = EntryForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request: HttpRequest):
        form = EntryForm(request.POST)
        if form.is_valid():
            create_entry_in_csv(form.cleaned_data)
            empty_form = EntryForm()
            return render(request, 'create.html', {'form': empty_form})

        return render(request, 'create.html', {'form': form})


def all_entries(request):
    entries = get_all_csv_entries()
    return render(request, 'list.html', {'entries': entries})

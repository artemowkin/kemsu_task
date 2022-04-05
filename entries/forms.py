from django import forms


COLORS_CHOICES = [
    ('красный', 'Красный'), ('зеленый', 'Зеленый'), ('синий', 'Синий')
]


class EntryForm(forms.Form):
    title = forms.CharField(
        min_length=3, max_length=120, required=True, label='Название'
    )
    weight = forms.IntegerField(
        min_value=1, max_value=500, required=True, label='Вес'
    )
    color = forms.ChoiceField(choices=COLORS_CHOICES, label='Цвет')

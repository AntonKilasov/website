from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название услуги'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Здесь, вы можете оставить дополнительные заметки, и оставить свой номер телефона, для обратной связи'
            }),
        }
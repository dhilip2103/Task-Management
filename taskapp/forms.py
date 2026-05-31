from django import forms
from django.utils import timezone
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title', 'description',
            'status', 'priority', 'due_date'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
     # Custom validation — title check
    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters!"
            )
        return title

    # Due date validation
    def clean_due_date(self):
        due = self.cleaned_data.get('due_date')
        if due and not self.instance.pk:
            if due < timezone.now().date():
                raise forms.ValidationError(
                    "Due date cannot be in the past!"
                )
        return due
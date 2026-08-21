from django import forms
from .models import Todo

class TaskForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields = [
            'task',
            'priority',
            'due_date',
        ]
        widgets = {
    'due_date': forms.DateInput(attrs={'type': 'date'})
}

        
    
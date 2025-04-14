# forms.py
from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title']  # Add other fields if needed

    def __init__(self, *args, **kwargs):
        super(ReminderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full border-gray-300 rounded-md shadow-sm py-2 px-3 focus:ring focus:ring-blue-200',
                'placeholder': f'Enter {field.label.lower()}'
            })

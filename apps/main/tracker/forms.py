from django import forms
from .models import Entry, SHAPE_CHOICES, COLOR_CHOICES

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'shape', 'color']
        widgets = {
            'shape': forms.Select(choices=SHAPE_CHOICES),
            'color': forms.Select(choices=COLOR_CHOICES),
        }
    
    # Custom validation example (Bonus Feature)
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name
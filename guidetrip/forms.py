from django import forms
from .models import trips, categories


class ProductForm(forms.ModelForm):

    class Meta:
        model = trips
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories_all = categories.objects.all()
        self.fields['rec_owner'].widget = forms.HiddenInput()  # Hide the rec_owner field
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories_all]

        self.fields['categories'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'
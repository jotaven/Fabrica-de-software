from django.forms import ModelForm
from .models import List

class RegistroList(ModelForm):
        class Meta:
            model = List
            fields = ['titulo', 'texto']
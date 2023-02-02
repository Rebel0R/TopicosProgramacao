from django.forms import ModelForm
from appPythonWeb.models import Carros

class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']
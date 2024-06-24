from django.forms import ModelForm
from patient.models import HeartVital

class HeartVitalForm(ModelForm):
    class Meta:
        model = HeartVital
        # fields = '__all__'
        exclude = ['user','HeartDisease','prediction_probability']

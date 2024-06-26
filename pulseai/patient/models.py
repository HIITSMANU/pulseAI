from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_OPTIONS = {
    'M' : 'Male',
    'F' : 'Female',
}

CHEST_PAIN_OPTIONS = {
    "TA": "Typical Angina", 
    "ATA": "Atypical Angina", 
    "NAP": "Non-Anginal Pain", 
    "ASY": "Asymptomatic"
}
BLOOD_SUGAR_OPTIONS = {
    '0':'less than or equal to 120',
    '1':'More than to 120'
}

ECG_OPTIONS = {
    "Normal": "Normal", 
    "ST": "having ST-T wave abnormality", 
    "LVH": "showing probable or definite left ventricular hypertrophy by Estes' criteria"
}

EXCERCISE_ANGINA_OPTIONS = {
    "Y": "Yes",
    "N": "No"
}

ST_SLOPE_OPTIONS = {
    "Up": "upsloping", 
    "Flat": "flat", 
    "Down": "downsloping"
}

HEART_DISEASE_OPTIONS = {
    "1": "heart disease",
    "0": "Normal"
}

APPOINTMENT_STATUS = {
    "Booked": "Booked",
    "Visited":"Visited",
    "Cancelled":"Cancelled"
}
class HeartVital(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=20, choices=GENDER_OPTIONS)
    ChestPainType = models.CharField(max_length=20,choices=CHEST_PAIN_OPTIONS)
    RestingBP = models.IntegerField(verbose_name="Resting Blood Pressure (60-220)")
    Cholesterol = models.IntegerField()
    FastingBS = models.CharField(max_length=20,choices=BLOOD_SUGAR_OPTIONS,verbose_name="Fasting Blood Pressure (60-900)")
    RestingECG = models.CharField(max_length=20,choices=ECG_OPTIONS,verbose_name="Resting ECG Condition")
    MaxHR = models.IntegerField(verbose_name="Maximum Heart Rate (60-220)")
    ExerciseAngina = models.CharField(max_length=20,choices=EXCERCISE_ANGINA_OPTIONS)
    Oldpeak = models.FloatField(verbose_name="Old peak(-2.5 - +2.5)")
    ST_Slope =  models.CharField(max_length=20,choices=ST_SLOPE_OPTIONS)
    HeartDisease = models.CharField(max_length=255,blank=True)
    prediction_probability = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.user.username
    

class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=20)
    date = models.DateField()
    note = models.TextField()
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS,default='Booked')

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
    
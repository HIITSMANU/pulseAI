from django.contrib import admin
from patient.models import HeartVital,Appointment

# Register your models here.



class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user','mobile','date','note','status')
    search_fields = ('user','mobile')
    list_filter = ('status','date')
    list_editable = ('status',)
    ordering = ('-date',)
    list_per_page = 25


admin.site.register(HeartVital)
admin.site.register(Appointment,AppointmentAdmin)

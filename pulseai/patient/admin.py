from django.contrib import admin
from patient.models import HeartVital,Appointment,Patient,Visit
from django_summernote.admin import SummernoteModelAdminMixin

# Register your models here.



class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user','mobile','date','note','status')
    search_fields = ('user','mobile')
    list_filter = ('status','date')
    list_editable = ('status',)
    ordering = ('-date',)
    list_per_page = 25

class VisitInline(SummernoteModelAdminMixin,admin.StackedInline):
    model = Visit
    extra = 1
    summernote_fields = ('diagnosis')

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    inlines = [VisitInline ,]
    raw_id_fields = ('patient',)

    list_display = ('patient','full_name')
    search_fields = ('patient__username','patient__first_name')


admin.site.register(HeartVital)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Patient,PatientAdmin)


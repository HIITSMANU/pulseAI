from django.urls import path
from patient import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    path("take_a_test/",views.take_a_test,name="test"),
    path("appointment/",views.appointment,name="appoint"),
    path("delete_appointment/<int:aid>/",views.delete_appointment,name="del_appoint"),
    path("update_appointment/<int:aid>/",views.update_appointment,name="updateapp")
]

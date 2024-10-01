from django.urls import path
from patient import views

urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    path("take_a_test/",views.take_a_test,name="test"),
    path("appointment/",views.appointment,name="appoint"),
    path("delete_appointment/<int:aid>/",views.delete_appointment,name="del_appoint"),
    path("update_appointment/<int:aid>/",views.update_appointment,name="updateapp"),
    path("profile/",views.profile_view,name="profile"),
    path('change-email/', views.change_email, name='change_email'),
    path('edit-password/', views.edit_password, name='edit_password'),
]
